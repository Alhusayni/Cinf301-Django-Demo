from django.contrib import admin

# Register your models here.
from studentdemo.models import Student, Degree

admin.site.register(Student)
admin.site.register(Degree)