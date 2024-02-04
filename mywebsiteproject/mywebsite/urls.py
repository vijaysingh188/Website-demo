from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from .scripts.homepage import homepageview,aboutpageview,servicepageview,contactpageview

urlpatterns = [
    path('', homepageview.as_view(), name='home'),
    path('about', aboutpageview.as_view(), name='about'),
    path('service', servicepageview.as_view(), name='service'),
    path('contact', contactpageview.as_view(), name='contact'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

