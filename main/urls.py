from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import *
urlpatterns = [
   
    path('', index,name='index'),
    path('about/', about,name='about'),
    path('contact/', contact,name='contact'),
    path('career/', career,name='career'),
    path('services/', services,name='services'),
    path("send-contact/", contact_form_submit, name="contact_form_submit"),
    path("send-career/", career_form_submit, name="career_form_submit"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)