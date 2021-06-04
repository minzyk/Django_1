from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# 원하는 뷰 생성 - 브라우저에서 접근하여 Hello World 생성


def hello_world(request):

    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html', context={'text': 'POST METHOD'})    # HttpResponse ('Hello world!')
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD'})

