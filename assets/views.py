from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Asset, PartUsage
from .forms import PartUsageForm
from utils.permissions import is_technician, is_manager, is_admin


# ✅ Public View — List of all assets
def asset_list(request):
    """
    Displays all available assets, ordered alphabetically.
    Accessible to any user.
    """
    assets = Asset.objects.all().order_by('name')
    return render(request, 'assets/asset_list.html', {
        'assets': assets
    })


@login_required
def asset_detail(request, pk):
    """
    Displays detailed info for a specific asset, including part usage.

    - All users can view asset and usage history.
    - Technicians, Managers, and Admins can log usage.
    """
    asset = get_object_or_404(Asset, pk=pk)
    part_usages = PartUsage.objects.filter(
        asset=asset
    ).order_by('-used_on')

    can_log_usage = (
        is_technician(request.user) or
        is_manager(request.user) or
        is_admin(request.user)
    )

    form = PartUsageForm() if can_log_usage else None

    if request.method == 'POST' and can_log_usage:
        form = PartUsageForm(request.POST)
        if form.is_valid():
            usage = form.save(commit=False)
            usage.asset = asset
            usage.taken_by = request.user  # Track who took the part
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
    Placeholder view for creating a user account.

    Only accessible to Managers and Admins.
    """
    return render(request, 'users/create_user.html')
