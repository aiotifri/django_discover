from django.db import models

# Create your models here.

class Category(models.Model):
    nom=models.CharField(max_length=100)
    description=models.TextField()

class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    img=models.ImageField(upload_to="task_img/")
    active=models.BooleanField(default=False)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)

# python manage.py runserver