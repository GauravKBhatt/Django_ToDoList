from django.urls import path
from .views import *

urlpatterns =[
    path('',GetRoutes.as_view()),
    path('items/',GetItems.as_view())
]