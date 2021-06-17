from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld
from accountapp.templates.decorators import account_ownership_required
# Create your views here.
# 원하는 뷰 생성 - 브라우저에서 접근하여 Hello World 생성


has_ownership = [login_required, account_ownership_required]


@login_required
def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('hello_world_input')       # POST라는 메소드의 hello_world_input 이름을 가진 데이터 요청

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()      # HelloWorld의 모든 객체들을 hello_world_list에 넣어준다
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        # reverse 함수를 이용해서 accountapp 내부의 hello_world 에 재접속하도록 만든다 (import 필요)
        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
        # HttpResponse ('Hello world!') / new_hello_world 로 내보내는 것
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


@method_decorator(has_ownership, 'get')    # 일반 decorator를 method에서 사용할 수 있게 해주는것으로 사용할 메소드의 이름을 적어준다
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User    # Django 기본 제공 user
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User    # Django 기본 제공 user
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'