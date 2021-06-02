from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# 원하는 뷰 생성 - 브라우저에서 접근하여 Hello World 생성


def hello_world(request):
    return render(request, 'base.html')    # HttpResponse ('Hello world!')