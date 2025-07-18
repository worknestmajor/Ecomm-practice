from django.urls import path
from . views import ProductView

urlpatterns =[
    path("products", ProductView.as_view()),
    path("products/<int:id>", ProductView.as_view())
]