from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    #path('', TemplateView.as_view(template_name='index.html')), 
    path('', views.home, name='home'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    # path('account/', views.accountSettings, name="account"),

    path('products/', views.products, name="products"),
]
