from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Project(models.Model):
    projectName = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    class Meta:
        permissions = (
            ('view_project', 'Can view project'),
        )

    def __str__(self):
        return self.projectName
