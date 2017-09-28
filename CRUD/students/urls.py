from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)

app_name = 'students'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<student_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
