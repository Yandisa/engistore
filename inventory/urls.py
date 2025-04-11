from django.urls import path
from . import views

# 🔗 URL patterns for inventory-related views
urlpatterns = [
    # 🧾 View list of all parts
    path(
        '',
        views.part_list,
        name='part_list'
    ),

    # 🔍 Detailed view for a specific part
    path(
        '<int:pk>/',
        views.part_detail,
        name='part_detail'
    ),

    # 📩 Request a new part (Technician/Viewer)
    path(
        'request-part/',
        views.request_part,
        name='request_part'
    ),

    # 📝 View all part requests by logged-in user
    path(
        'my-requests/',
        views.my_part_requests,
        name='my_part_requests'
    ),
]
