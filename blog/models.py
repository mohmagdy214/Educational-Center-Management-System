from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from ecms_app.models import Student

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=30000)
    create_date = models.DateTimeField(default=timezone.now)
    draft = models.BooleanField(default=True)
    tags = TaggableManager()
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='post_teacher')
    image =  models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='comment_teacher')
    # student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True, related_name='comment_student')
    post = models.ForeignKey(Post, related_name='comment_post', on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)
