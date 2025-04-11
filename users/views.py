from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from utils.permissions import is_manager, is_admin


@login_required
@user_passes_test(lambda u: is_manager(u) or is_admin(u))
def create_user(request):
    """
    Create a new user and assign them to a role (group).
    Only accessible to Managers and Admins.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Prevent duplicate usernames
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'User already exists.')
        else:
            user = User.objects.create_user(
                username=username,
                password=password
            )
            try:
                # Assign user to the selected group/role
                group = Group.objects.get(name=role)
                user.groups.add(group)
                messages.success(
                    request,
                    f'User "{username}" created and added to group "{role}".'
                )
            except Group.DoesNotExist:
                messages.error(request, f'The group "{role}" does not exist.')

        return redirect('create_user')

    # Load all available roles for dropdown
    roles = Group.objects.all()
    return render(request, 'users/create_user.html', {'roles': roles})
