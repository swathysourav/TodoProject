from typing import Any
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    description = models.TextField(null=True)
    created_date = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title