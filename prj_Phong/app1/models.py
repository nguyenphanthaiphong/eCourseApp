from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass


class Lesson(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=50, null = False)

    def __str__(self):
        return  self.name

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['-id']


class Course(BaseModel):
    subject = models.CharField(max_length = 255, null= False)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='app1/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

class Interaction(BaseModel):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete= models.CASCADE)
    class Meta:
        abstract = True

class Comment(Interaction):
    content = models.CharField(max_length= 255)

class Like(Interaction):
    class Meta:
        unique_together = ('user', 'lesson')