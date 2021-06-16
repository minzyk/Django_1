from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

from accountapp.models import HelloWorld

# Create your views here.
# 원하는 뷰 생성 - 브라우저에서 접근하여 Hello World 생성


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')       # POST라는 메소드의 hello_world_input 이름을 가진 데이터 요청

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        
        hello_world_list = HelloWorld.objects.all()      # HelloWorld의 모든 객체들을 hello_world_list에 넣어준다
        return HttpResponseRedirect(reverse('accountapp:hello_world'))        # reverse 함수를 이용해서 accountapp 내부의 hello_world 에 재접속하도록 만든다 (import 필요)
        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})    # HttpResponse ('Hello world!') / new_hello_world 로 내보내는 것
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User    # Django 기본 제공 user
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')    # reverse는 함수형 -> 그대로 사용하면 안되고 클래스형에서는 reverse_lazy 를 사용
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
