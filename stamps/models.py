from django.db import models
from django.conf import settings

# Create your models here.
class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    target_amount = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    
class Daily(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    success = models.BooleanField(default=False)
    memo = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
