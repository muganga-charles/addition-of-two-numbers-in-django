
from django.urls import path
from . import views
urlpatterns= [
    path('', views.stating, name="stat"),
    path('add', views.add, name='add'),
]