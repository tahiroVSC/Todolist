from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin


from apps.todo.models import Todo
from apps.todo.serializers import ToDoSerializer

# Create your views here.
class ToDoAPIViewSet(GenericViewSet,
                     ListModelMixin,
                     RetrieveModelMixin, 
                     CreateModelMixin, 
                     UpdateModelMixin, 
                     DestroyModelMixin):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer