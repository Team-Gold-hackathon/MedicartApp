from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    #path('', TemplateView.as_view(template_name='index.html')), 
    path('', views.home, name='home')
]
