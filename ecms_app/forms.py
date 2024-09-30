from django import forms
from .models import Student, TeacherProfile


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('teacher',)

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        exclude = ('teacher',)
