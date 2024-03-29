from django.db import models
from datetime import datetime
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return self.title
