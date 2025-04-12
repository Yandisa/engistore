from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from utils.permissions import is_manager, is_admin


@login_required
@user_passes_test(lambda u: is_manager(u) or is_admin(u))
def create_user(request):
    """
    Allows Managers and Admins to create new user accounts.

    Users can be assigned to one of the existing roles (groups).
    Handles validation for duplicate usernames and group existence.
    """
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        role = request.POST.get('role', '').strip()

        if User.objects.filter(username=username).exists():
            messages.warning(request, '⚠️ User already exists.')
        else:
            user = User.objects.create_user(
                username=username,
                password=password
            )
            try:
                group = Group.objects.get(name=role)
                user.groups.add(group)
                messages.success(
                    request,
                    f'✅ User "{username}" added to group "{role}".'
                )
            except Group.DoesNotExist:
                messages.error(
                    request,
                    f'❌ Group "{role}" does not exist.'
                )

        return redirect('create_user')

    # Display available roles in the form
    roles = Group.objects.all()
    return render(request, 'users/create_user.html', {'roles': roles})
