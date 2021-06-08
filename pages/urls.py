from django.urls import path
from .views import Homepageview

urlpatterns = [
  path('', Homepageview.as_view(),name='home'),
]