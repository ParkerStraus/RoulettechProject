from django.urls import path
from .views import add_contact, delete_contact, list_contacts

urlpatterns = [
    path('add/', add_contact, name='add_contact'),
    path('delete/<int:pk>/', delete_contact, name='delete_contact'),
    path('list/', list_contacts, name='list_contacts'),
]
