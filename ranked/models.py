from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SixMans(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    elo = models.IntegerField()
    mmr = models.IntegerField()
    rank = models.CharField(max_length=25)
    def __str__(self):
        return self.user.username
