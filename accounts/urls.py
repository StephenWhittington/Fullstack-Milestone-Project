from django.conf.urls import url, include
from . import url_reset
from .views import index, logout, login, registration, customer, create_or_edit_customer


urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="registration"),
    url(r'^customer/$', customer, name='customer'),
    url(r'^new/$', create_or_edit_customer, name='new_details'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_customer, name='edit_customer'),
    url(r'^password-reset/', include(url_reset)),
]