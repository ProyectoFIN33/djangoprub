from django.urls import path 
from . import views
urlpatterns = [
    path('', views.homepage),
    path('about/', views.about),
    
# urls.py



    
]