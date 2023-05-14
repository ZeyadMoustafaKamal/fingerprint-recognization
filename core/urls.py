from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('scan/',views.scan,name='scan'),
    path('view/',views.view_results,name='view_data')
]
