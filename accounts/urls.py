from django.conf.urls import url, include
from . import url_reset
from .views import index, logout, login, registration


urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="registration"),
    url(r'^password-reset/', include(url_reset)),
]