from django.db import models
from django.forms import CharField

# Create your models here.
class Task(models.Model):
    tittle = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.tittle
