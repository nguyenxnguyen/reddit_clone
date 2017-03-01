from django.db import models

# Create your models here.
class user_activity(models.Model):
    users_posts = models.CharField(max_length=200)
    users_votes = models.CharField(max_length=200)