from django.db import models

# Create your models here.
class Todo(models.Model):
    id =  models.AutoField(
        primary_key = True
    )
    title = models.CharField(
        max_length = 100,
        verbose_name = "Название"
    )
    description = models.TextField(
        verbose_name = "Описание"
    )
    completed = models.BooleanField(
        verbose_name="Статус",
        default=False
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__ (self):
        return self.title

    class Meta:
        verbose_name = "Todo List",
        verbose_name_plural = "Todo List"