from django.contrib import admin
from .models import Student, TeacherProfile, Material

# Register your models here.


admin.site.register(Student)
admin.site.register(TeacherProfile)
admin.site.register(Material)
