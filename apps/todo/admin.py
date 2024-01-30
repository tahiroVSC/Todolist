from django.contrib import admin

from apps.todo.models import Todo
# Register your models here.
@admin.register(Todo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['title', 'completed', 'created']
    