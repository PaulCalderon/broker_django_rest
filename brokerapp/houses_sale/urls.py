from django.urls import path, include
from . import views


urlpatterns = [
    
    path('', views.house_list),
    path('details/<int:pk>', views.house_detail),
]
