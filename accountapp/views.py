from django.http import HttpResponse
from django.shortcuts import render
from accountapp.models import HelloWorld

# Create your views here.
# 원하는 뷰 생성 - 브라우저에서 접근하여 Hello World 생성


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')       # POST라는 메소드의 hello_world_input 이름을 가진 데이터 요청

        new_hello_world = hello_world()
        new_hello_world.text = temp
        new_hello_world.save()

        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})    # HttpResponse ('Hello world!') / new_hello_world 로 내보내는 것
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD'})

