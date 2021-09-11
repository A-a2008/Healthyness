from django.db import models
from django.db.models import Model
from django.contrib.auth import get_user_model

# Create your models here.


class Yoga(Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='+')
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.first_name



