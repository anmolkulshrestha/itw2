from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from  .models import Student
        
def student_home(request):
    if request.user.is_authenticated:
        student = Student.objects.get(roll=request.user.username)
        return render(request, 'accounts/student_home.html', {"student": student})
    else:
        return redirect('login')
    
def login_user(request):
    if request.method == 'POST':
        roll=request.POST['roll']
        passwd=request.POST['password']
        user = authenticate(request, username=roll, password=passwd)
        print(roll, passwd, user)
        if user is not None:
            # login
            login(request, user)
            return redirect('student_home')
        else:
            #Not login
            return render(request, 'accounts/login.html', {"error": True})
    else:
        return render(request, 'accounts/login.html')
        
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')
