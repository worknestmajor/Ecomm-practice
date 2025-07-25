from django.urls import path
from . views import CategoryView

urlpatterns =[
    path("category", CategoryView.as_view(),name='category'),
    path("category/<int:id>", CategoryView.as_view(),name='category-detail')
]