from django.urls import path
from .views import *

urlpatterns =[
    path('',home.as_view(),name="home"),
    path('home/',home.as_view(),name="home"),
    path('item/<str:pk>',itemview.as_view(),name="item"),
    path('create/',create.as_view(),name="create"),
    path('update/',update.as_view(),name="update"),
    path('delete/<int:pk>',delete.as_view(),name="delete")
]