from django.conf.urls import url
from backend import views

urlpatterns = [
    url(r'^create_deal/$', views.create_client_contact_deal),
]