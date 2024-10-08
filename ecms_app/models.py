from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
from django.utils import timezone

# Create your models here.


class TeacherProfile(models.Model):
    teacher = models.OneToOneField(User, related_name='teacher_profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='teacher_profile_images')
    about_me = models.TextField(max_length=5000, null=True, blank=True)
    phone = models.IntegerField(unique=True)
    material = models.ForeignKey('Material', related_name='teacher_material', on_delete=models.SET_NULL, null=True, blank=True)
    t_code = models.CharField(max_length=8, default=generate_code, unique=True)
    facebook_link = models.URLField(max_length=200, null=True, blank=True)
    twitter_link = models.URLField(max_length=200, null=True, blank=True)
    insta_link = models.URLField(max_length=200, null=True, blank=True)
    address = models.TextField(max_length=500, null=True, blank=True)
    birthday = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.teacher)


class Student(models.Model):
    name = models.CharField(max_length=250)
    teacher = models.ForeignKey(User, related_name='teacher_students', on_delete=models.SET_NULL, null=True, blank=True)
    s_code = models.CharField(max_length=10, default=generate_code, unique=True)
    material = models.ForeignKey('Material', related_name='student_material', on_delete=models.SET_NULL, null=True, blank=True)
    age = models.IntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Material(models.Model):
    material_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.material_name
