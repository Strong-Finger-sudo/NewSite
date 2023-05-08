from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path

from testsite import settings
from .views import *

urlpatterns = [
    path('', BeautysalonHome.as_view(), name='home'),
    path('about/', BeautysalonAbout.as_view(), name='about'),
    path('contacts/', BeautysalonContacts.as_view(), name='contacts'),
    path('services', BeautysalonServices.as_view(), name='services'),
]
