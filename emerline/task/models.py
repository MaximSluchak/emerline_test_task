
from django.contrib.auth.models import User
from django.db import models

from emerline.project.models import Project


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    dueDate = models.DateTimeField()
    user = models.ForeignKey(User)
    projects = models.ForeignKey(Project, null=True, blank=True)

    class Meta:
        permissions = (
            ('view_task', 'Can view task'),
        )

    def __str__(self):
        return self.title
