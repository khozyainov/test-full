from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True, blank=True)
    author = models.ForeignKey('auth.User', related_name='blogs', on_delete=models.CASCADE)
