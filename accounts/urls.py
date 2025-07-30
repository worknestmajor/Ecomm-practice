from django.urls import path
from .views import RegisterView, AdminView, LoginView, CreateStaffView,LogoutView,DeleteStaffView

urlpatterns =[
    path('auth', RegisterView.as_view(), name ="auth"),
    path('auth/login', LoginView.as_view()),
    path('auth/admin', AdminView.as_view()),
    path('auth/admin/staff' , CreateStaffView.as_view()),
    path('auth/logout' , LogoutView.as_view()),
    path('auth/admin/delete-staff/<str:username>', DeleteStaffView.as_view())
]