from django.db import models

# Create your models here.


class Question(models.Model):
    question_test = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date')

    def __str__(self):
        return self.question_test + self.pub_date


class Choice(models.Model):
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text + self.votes