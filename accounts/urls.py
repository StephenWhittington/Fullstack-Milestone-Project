from django.conf.urls import url, include
from . import url_reset
from .views import index, logout, login, registration, customer, edit_customer, new_details


urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="registration"),
    url(r'^customer/$', customer, name='customer'),
    url(r'^new/$', new_details, name='new_details'),
    url(r'^(?P<pk>\d+)/edit/$', edit_customer, name='edit_customer'),
    url(r'^password-reset/', include(url_reset)),
]