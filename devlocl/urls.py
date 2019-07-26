from django.conf.urls import url, include
from .views import index, report, login_view, logout_view, send_view, solit
from django.urls import path, URLPattern



urlpatterns = [
    path("", login_view, name='login_view'),
    path("solit/", solit, name='solit'),
    path("index/", index, name= 'index'),
    path("report/", report, name='report'),
    path("logout_view/", logout_view, name='logout_view'),
    path("send_view/", send_view, name='send'),

]