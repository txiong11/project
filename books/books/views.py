from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout #this use for login and logout


def home_view(request):
    user = request.user
    hello = 'Home'

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'main/home.html', context)
    # return HttpResponse('Hello world')

#add this for the login 
def user_login(request):
    pass