from django.shortcuts import render
from django.http import HttpResponse
from studentdemo import models
# Create your views here.

def index(request):
    test={'name': 'Abdul',
          'age': 21,
          'country': 'saudi'}

    return render(request,'index.html', test )
    #return  HttpResponse('Welcome dude')


def student(request):
    studento = models.Student.objects.all()
    context= {'stu': studento}
    return render(request, 'student.html',context)
   #return  HttpResponse('student dude')


def degree(request, student_id):
    degreo = models.Degree.objects.filter(student_id = student_id)
    context = {'deg': degreo}
    return render(request, 'degree.html', context)
    #return  HttpResponse('Your ID is :' + student_id)
