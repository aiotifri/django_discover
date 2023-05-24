from django.contrib import admin

# Register your models here.
from home.models import Task, Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title',"active"]
    list_editable = ['active']


@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    pass