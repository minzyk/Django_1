from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),     # Django에서 기본 제공하는 User를 사용하여 간편하게 구현
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),    # as_view() 함수는 클래스의 인스턴스를 생성하고, 인스턴스의 dispatch() 메소드를 호출
]