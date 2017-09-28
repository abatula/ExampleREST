from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'students'
urlpatterns = [
    url(r'^$', views.student_list),
    url(r'^(?P<student_id>[0-9]+)/$', views.student_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
