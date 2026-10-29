from django.db import models

class Poll(models.Model):
    language = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.language

# Create your models here.
