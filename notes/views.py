from django.shortcuts import render
from .models import Notes
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers

@login_required(login_url='/login/')


def index(request):
    if request.method == 'POST':
        new_note = Notes.objects.create(text=request.POST['newnote'])
        serializers_obj = serializers.serialize('json', [new_note])
        return JsonResponse(serializers_obj[1:-1], safe=False)
    return render(request, 'notes/index.html')

def login_view(request):
    
    redirect = request.GET.get('next')
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('redirect'))
        else:
            return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect})
    return render(request, 'auth/login.html', {'redirect': redirect})


def registration_view(request):
    """
    This is the view for the Register Page
    """
    redirect = request.GET.get('next')
    if request.method == 'POST':
        try:
            
            user = User.objects.create_user(username=request.POST.get('register-username'), password=request.POST.get('register-password'))
            user.save()
            return HttpResponseRedirect(request.POST.get('redirect'))
        except:
            return render(request, 'auth/registration.html', {'redirect': redirect, 'error': 'Benutzer konnte nicht angelegt werden'})
    return render(request, 'auth/registration.html', {'redirect': redirect})


def logout_view(request):
    """
    This is the view for the Logout
    """
    logout(request)
    return HttpResponseRedirect('/login')