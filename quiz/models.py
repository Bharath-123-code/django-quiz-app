from django.db import models

class Question(models.Model):
    question_text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

class HighScore(models.Model):
    player_name = models.CharField(max_length=100)
    score = models.IntegerField()
    date_achieved = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score', '-date_achieved']