from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Asset, PartUsage
from .forms import PartUsageForm
from utils.permissions import is_technician, is_manager, is_admin


@login_required
def asset_list(request):
    """
    View to list all assets in the system.
    Accessible by all authenticated users.
    """
    assets = Asset.objects.all()
    return render(request, 'assets/asset_list.html', {'assets': assets})


@login_required
def asset_detail(request, pk):
    """
    View the details and part usage history of a specific asset.
    - All users can view asset details.
    - Technicians, Managers, and Admins can log part usage.
    """
    asset = get_object_or_404(Asset, pk=pk)
    part_usages = PartUsage.objects.filter(asset=asset).order_by('-used_on')
    can_log_usage = (
        is_technician(request.user)
        or is_manager(request.user)
        or is_admin(request.user)
    )

    form = PartUsageForm() if can_log_usage else None

    if request.method == 'POST' and can_log_usage:
        form = PartUsageForm(request.POST)
        if form.is_valid():
            usage = form.save(commit=False)
            usage.asset = asset
            usage.taken_by = request.user  # Track who logged the usage
            usage.save()
            return redirect('asset_detail', pk=asset.pk)

    return render(request, 'assets/asset_detail.html', {
        'asset': asset,
        'part_usages': part_usages,
        'form': form,
        'can_log_usage': can_log_usage,
    })


@login_required
@user_passes_test(lambda u: is_manager(u) or is_admin(u))
def create_user(request):
    """
    Placeholder view for creating a new user.
    - Only Managers and Admins can access.
    """
    return render(request, 'users/create_user.html')
