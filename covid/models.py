from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Questions(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_ques")
    ques = models.CharField(max_length=2048, help_text="Your question!")

    def __str__(self):
        return f'{self.ques} by {self.author}'

class Answers(models.Model):
    ans = models.CharField(max_length=2048)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name="answers")

    def __str__(self):
        return f"{self.ans} for question: {self.question}"

