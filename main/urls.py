from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
    path('about/', views.about, name='about'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('contact/', views.contact_view, name='contact'),

]