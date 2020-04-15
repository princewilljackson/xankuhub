from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name = 'xanku'
urlpatterns = [
    path('', views.home, name='home'),
    path('item/', views.item_details, name='item_name'),
    path('description/', views.item_description, name='item_description'),
    path('owner/', views.item_owner, name='item_owner'),
    path('contact/', views.owner_contact, name='owner_contact'),
]