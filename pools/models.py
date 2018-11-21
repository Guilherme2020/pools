from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    closed = models.BooleanField(default=False)
    pub_datee = models.DateField()

class Choise(models.Model):
    question = models.ForeignKey(Question,null=True, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=255,null=True)
    votes = models.IntegerField()

    def __str__(self):
        return self.choise_text