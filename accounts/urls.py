from django.urls import path
from .views import RegisterView,InfoView

urlpatterns =[
    path('auth', RegisterView.as_view()),
    path('auth/info', InfoView.as_view())
]