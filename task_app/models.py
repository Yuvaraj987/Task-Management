from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    Task_Name = models.CharField(max_length=200)
    Description = models.TextField(null=True, blank=True)
    Status = models.BooleanField(default=False)
    Create_Date = models.DateField(auto_now_add=True)
    Create_Time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.Task_Name

    class Meta:
        ordering = ['Status']