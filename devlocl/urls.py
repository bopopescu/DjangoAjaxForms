from django.conf.urls import url, include
from .views import index, solit, report, login_view, logout_view, send_view, adicion
from django.urls import path


urlpatterns = [
    path("", login_view, name='login_view'),
    path("index/", index, name= 'index'),
    path("report/", report, name='report'),
    path("solit/", solit, name='solit'),
    path("adicion/", adicion, name='adicion'),
    path("logout_view/", logout_view, name='logout_view'),
    path("send_view/", send_view, name='send'),
]