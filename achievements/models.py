from django.db import models
from django.conf import settings


class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Achievement(models.Model):
    goal = models.ForeignKey(Goal)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=200)
    count = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content