from django.urls import path

from . import views


app_name = 'annotask'

urlpatterns = [
    path('', views.new, name='index'),
    path('new/', views.new, name='new_task'),
]