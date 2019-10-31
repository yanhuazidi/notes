
from django.conf.urls import url
from userinfo import views

urlpatterns = [
    url(r'registerh',views.register_,name="registerh"),
    url(r'loginh',views.login_,name="loginh"),
]
