from django.urls import path

from landing.views import *

#  The urls of the landing page
app_name = 'landing'
urlpatterns = [
    path('contact', ContactCreateView.as_view(), name='contact'),
    path('locations', LocationListView.as_view(), name='contact'),
]
