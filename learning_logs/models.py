'''Model'''
# Each Model - type, relationship

from django.db import models

# Create your models here.
class Topic(models.Model):
    EASY = "easy"
    NORMAL = "normal"
    HARD = "hard"

    level_choices = (
        (EASY, "easy"),
        (NORMAL, "normal"),
        (HARD, "hard"),
    )

    text = models.CharField(max_length=200, null=False, blank=False, unique=True)
    level = models.CharField(max_length=10, choices= level_choices, default=EASY)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # if you want to refer more than on Entry
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}"


