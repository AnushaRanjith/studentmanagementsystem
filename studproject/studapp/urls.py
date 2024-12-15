from django.urls import path, include
from django.urls import path
from .views import AdminDashboard, OfficeStaffDashboard, LibrarianDashboard,LoginView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('api/token/', obtain_auth_token, name='obtain_token'),  # Standard DRF token authentication
    path('login/', LoginView.as_view(), name='login'),  # Custom login view
    path('admin_dashboard/', AdminDashboard.as_view(), name='admin_dashboard'),
    path('office_staff_dashboard/', OfficeStaffDashboard.as_view(), name='office_staff_dashboard'),
    path('librarian_dashboard/', LibrarianDashboard.as_view(), name='librarian_dashboard'),
]

