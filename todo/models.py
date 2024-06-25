from django.db import models

# Create your models here.
class Todo(models.Model):

    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'
    IMPORTANCE_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    completed = models.BooleanField()
    duration = models.IntegerField()
    importance = models.CharField(max_length=6, choices=IMPORTANCE_CHOICES)

    def __str__(self) -> str:
        return self.title