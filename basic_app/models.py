from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    question = models.CharField(max_length = 200)
    choice_one = models.CharField(max_length = 200)
    choice_two = models.CharField(max_length = 200)
    choice_three = models.CharField(max_length = 200)
    choice_four = models.CharField(max_length = 200)
    choice_five = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.question

class Scorrer(models.Model):
    owner = models.ForeignKey(User, related_name='books',default=None,on_delete=models.PROTECT)
    scored = models.CharField(max_length=200)