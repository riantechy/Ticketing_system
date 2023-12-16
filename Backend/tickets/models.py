# tickets/models.py
from django.db import models

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    problem_details = models.TextField()
    priority = models.CharField(max_length=20)

    def __str__(self):
        return self.title
