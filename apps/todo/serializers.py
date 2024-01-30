from rest_framework import serializers

from apps.todo.models import Todo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'created')