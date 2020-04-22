from django.conf.urls import url
from .views import get_comments, comment_detail, create_or_edit_comment

urlpatterns = [
    url(r'^$', get_comments, name='get_comments'),
    url(r'^(?P<pk>\d+)/$', comment_detail, name='comment_detail'),
    url(r'^new/$', create_or_edit_comment, name='new_comment'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_comment, name='edit_comment')
]