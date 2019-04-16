from django.shortcuts import render
from django.http import HttpResponse
from studentdemo import models
from studentdemo import forms


# Create your views here.
def httres(request):
    return HttpResponse('Welcome, CINF301')


def index(request):
    test = {'name': 'Abdul',
            'age': 21,
            's': 'Student'}

    return render(request, 'index.html', test)


def student(request):
    studento = models.Student.objects.all()
    context = {'stu': studento}
    return render(request, 'student.html', context)


""""
def degree(request, student_id):
    degreo = models.Degree.objects.filter(student_id = student_id)
    context = {'deg': degreo}
    return render(request, 'degree.html', context)
"""


def register(request):
    form_data = forms.UserRegistrar(request.POST or None)
    msg = ''
    if form_data.is_valid():
        newstudent = models.Student()
        newstudent.first_name = form_data.cleaned_data['first_name']
        newstudent.last_name = form_data.cleaned_data['last_name']
        newstudent.age = form_data.cleaned_data['age']
        newstudent.birth = form_data.cleaned_data['date_of_birth']
        newstudent.save()
        msg = 'New Student has been added!!'
    context = {
        'formregistor': form_data,
        'msg': msg
    }
    return render(request, 'register.html', context)


def degree(request, student_id):
    degreo = models.Degree.objects.filter(student_id=student_id)
    stid = models.Student.objects.get(id=student_id)
    form_data = forms.DegreeRegistrar(request.POST or None)
    msg = ''
    if form_data.is_valid():
        newdegree = models.Degree()
        newdegree.student_id = stid
        newdegree.student_degree = form_data.cleaned_data['Student_Degree']
        newdegree.save()
        msg = 'New degree has been added !!'
    context = {'deg': degreo,
               'formregister': form_data,
               'name': stid,
               'msg': msg}
    return render(request, 'degree.html', context)
