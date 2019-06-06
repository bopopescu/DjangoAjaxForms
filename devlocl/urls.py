from django.conf.urls import url, include
from .views import index, report, login_view, logout_view, send_view
from django.urls import path
from rest_framework import routers
from .viewsets import UserViewSet 

router = routers.SimpleRouter()
router.register('devlocl', UserViewSet)


urlpatterns = [
    path("", login_view, name='login_view'),
    path("index/", index, name= 'index'),
    path("report/", report, name='report'),
    path("logout_view/", logout_view, name='logout_view'),
    path("send_view/", send_view, name='send'),
]