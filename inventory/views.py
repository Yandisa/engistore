from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, F
from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_http_methods
from django.db import transaction
from django.contrib.auth.decorators import login_required

from .models import Part, Category, PartRequest
from assets.models import Asset, PartUsage
from utils.permissions import is_technician, is_manager, is_admin


# ✅ Public view — list all parts
def part_list(request):
    """
    Displays all parts in inventory.
    Allows search and filtering by category and low stock.
    """
    query = request.GET.get('q')
    category_id = request.GET.get('category')

    parts = Part.objects.all()
    categories = Category.objects.all()

    if query:
        parts = parts.filter(
            Q(name__icontains=query) |
            Q(part_number__icontains=query)
        )

    if category_id:
        parts = parts.filter(category_id=category_id)

    if request.GET.get('low_stock') == '1':
        parts = parts.filter(quantity__lte=F('reorder_threshold'))

    return render(request, 'inventory/part_list.html', {
        'parts': parts,
        'categories': categories,
        'selected_category': category_id,
        'query': query,
    })


# 📊 Dashboard view (basic stats + latest activity)
def dashboard(request):
    """
    Displays system stats and user-specific widgets on login.
    Accessible to all; more data shown to authenticated users.
    """
    total_parts = Part.objects.count()
    total_assets = Asset.objects.count()
    low_stock_count = Part.objects.filter(
        quantity__lte=F('reorder_threshold')
    ).count()
    recent_parts = Part.objects.order_by('-date_added')[:5]
    unused_parts_count = Part.objects.filter(partusage__isnull=True).count()

    # Default UI values
    recent_usage = []
    part_requests = []
    user_group = None
    can_add_user = False
    can_request_part = False
    is_logged_in = request.user.is_authenticated

    if is_logged_in:
        recent_usage = PartUsage.objects.select_related(
            'part', 'asset'
        ).order_by('-used_on')[:5]

        if request.user.groups.exists():
            user_group = request.user.groups.first().name

        if is_admin(request.user) or is_manager(request.user) \
                or request.user.is_superuser:
            can_add_user = True
            part_requests = PartRequest.objects.filter(reviewed=False)

        if is_technician(request.user) or user_group == "Viewer":
            can_request_part = True

    return render(request, 'dashboard.html', {
        'total_parts': total_parts,
        'total_assets': total_assets,
        'low_stock_count': low_stock_count,
        'recent_parts': recent_parts,
        'unused_parts_count': unused_parts_count,
        'recent_usage': recent_usage,
        'part_requests': part_requests,
        'can_add_user': can_add_user,
        'can_request_part': can_request_part,
        'user_group': user_group,
        'is_logged_in': is_logged_in,
    })


# 📦 Part detail & "take part from stock"
@login_required
@require_http_methods(["GET", "POST"])
def part_detail(request, pk):
    """
    View part details, stock, and usage history.
    Logged-in users with permissions can deduct stock.
    """
    part = get_object_or_404(Part, pk=pk)
    usage_logs = PartUsage.objects.filter(
        part=part
    ).order_by('-used_on')

    general_asset, _ = Asset.objects.get_or_create(
        name="General",
        code="GEN-000",
        defaults={"description": "Used when not linked to an asset"}
    )

    asset_queryset = Asset.objects.exclude(
        pk=general_asset.pk
    ) | Asset.objects.filter(pk=general_asset.pk)

    can_take_part = (
        is_technician(request.user) or
        is_manager(request.user) or
        is_admin(request.user)
    )

    form = TakePartForm()
    form.fields['asset'].queryset = asset_queryset

    if request.method == 'POST' and can_take_part:
        form = TakePartForm(request.POST)
        form.fields['asset'].queryset = asset_queryset

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            asset = form.cleaned_data['asset']

            if part.quantity <= 0:
                messages.error(request, "This part is out of stock.")
            elif quantity > part.quantity:
                messages.error(
                    request,
                    f"Only {part.quantity} unit(s) available."
                )
            else:
                try:
                    with transaction.atomic():
                        part.quantity -= quantity
                        part.save()

                        PartUsage.objects.create(
                            asset=asset,
                            part=part,
                            quantity_used=quantity,
                            taken_by=request.user
                        )

                    messages.success(
                        request,
                        f"{quantity} unit(s) of '{part.name}' taken "
                        f"for asset '{asset.name}'."
                    )
                    return redirect('part_detail', pk=part.pk)

                except ValidationError as e:
                    messages.error(request, e)

    return render(request, 'inventory/part_detail.html', {
        'part': part,
        'usage_logs': usage_logs,
        'form': form,
        'can_take_part': can_take_part,
    })


# 📩 Part request form
@login_required
def request_part(request):
    """
    Allows technicians and viewers to submit new part requests.
    """
    if request.method == 'POST':
        form = PartRequestForm(request.POST)
        if form.is_valid():
            part_request = form.save(commit=False)
            part_request.requested_by = request.user
            part_request.save()
            messages.success(
                request, "✅ Part request submitted successfully."
            )
            return redirect('dashboard')
    else:
        form = PartRequestForm()

    return render(request, 'inventory/request_part.html', {
        'form': form
    })


# 📝 View part request history for logged-in user
@login_required
def my_part_requests(request):
    """
    Displays a list of part requests made by the logged-in user.
    """
    requests = PartRequest.objects.filter(
        requested_by=request.user
    ).order_by('-created_at')
    return render(request, 'inventory/my_part_requests.html', {
        'requests': requests
    })


# 📘 About page (static)
def about(request):
    """
    About page with project information and system overview.
    """
    return render(request, 'about.html')


# 🔧 Form for taking a part from stock
class TakePartForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    asset = forms.ModelChoiceField(
        queryset=Asset.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )


# 📩 Form for requesting a new part
class PartRequestForm(forms.ModelForm):
    class Meta:
        model = PartRequest
        fields = ['name', 'part_number', 'quantity_needed', 'reason']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'part_number': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity_needed': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'reason': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
        }
