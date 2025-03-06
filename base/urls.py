from django.urls import path
from .views import *

urlpatterns =[
    path('',home.as_view(),name="home"),
    path('item/',item.as_view(),name="item"),
    path('create/',create.as_view(),name="create"),
    path('update/',update.as_view(),name="update"),
    path('delete/',delete.as_view(),name="delete")
]