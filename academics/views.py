from django.shortcuts import render, redirect
from .models import *
from .forms import ContactUsForm
from django.utils import timezone
from accounts.models import Student

"""
    This module contains the methods and classes to handle HTTPRequest and 
    generate appropriate HTTPResponse.
"""


def program(request, code):
    """
    :type request: HTTPRequest
    :param request: carries request info

    :type code: int
    :param code: program code

    -> filters out the program on the basis of given program code

    -> if no program exists with that code, return 404

    -> otherwise, render program.html with context current_program


    """
    try:
        current_program = Program.objects.get(code=code)
        return render(request, 'academics/program.html', {'current_program': current_program})
    except:
        return render(request, 'academics/404.html', {'error': '404 Page Not Found '})
        


    


def index(request):
    """

    :type request: HTTPRequest
    :param request: carries request info
    :return: renders index.html

    """
    return render(request, 'academics/index.html')


def facility(request):
    """

        :type request: HTTPRequest
        :param request: carries request info
        :return: renders facilities.html

        """
    return render(request, 'academics/facilities.html')


def scholarship(request):
    """

        :type request: HTTPRequest
        :param request: carries request info
        :return: renders scholarship.html

        """
    return render(request, 'academics/scholarship.html')


def handle404(request):
    """

           :type request: HTTPRequest
           :param request: carries request info
           :return: renders 404.html

    """
    return render(request, 'academics/404.html', {'error': '404 Page Not Found'})


def about_us(request):
    return render(request, 'academics/about.html')


def contact_us(request):
    if request.user.is_authenticated:
        newform = ContactUsForm()
        if request.method=='POST':
            form = ContactUsForm(data=request.POST)
            if form.is_valid():
                student=Student.objects.get(roll=request.user.username)
                message = form.save(commit=False)
                message.date = timezone.now()
                message.name=student.name
                message.email=student.email
                message.roll=student.roll
                message.save()
                return render(request, 'academics/contact-us.html', {'success' : True,'form':newform})
            else:
                return render(request, 'academics/contact-us.html', {'form' : form})
        else:
            return render(request, 'academics/contact-us.html', {'form' : newform})
    else:
        return redirect('login')
        
def grades(request):
    if request.user.is_authenticated:
        grades=Grades.objects.filter(roll=request.user.username)
        data=[]
        for i in range(8):
            data.append({'field': [], 'credits': 0, 'sem': 8-i})
        for grade in grades:
            data[8-grade.sem]['credits']+=grade.subject.credit
            data[8-grade.sem]['field'].append({'subject': grade.subject, 'grade': grade.grade})
        print(grades, credits)
        # return redirect('index')
        return render(request, 'academics/result.html', {'data': data, 'credits': credits, 'roll': request.user.username})
    else:
        return redirect('login')
        
def attendance(request):
    if request.user.is_authenticated:
        pass
    else:
        pass
    
def classes(request):
    if request.user.is_authenticated:
        pass
    else:
        pass
    


