from django.urls import path
from . import views

app_name = 'core'

urlpatters = [
    path('', views.index, name = 'index'),
    path('contact/', views.contact, name = 'contact'),
    path('signup/', views.signup, name = 'signup')
]