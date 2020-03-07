from django.db import models
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()

    def get_absolute_url(self):
        return reverse("blog:all_blogs")

    def __str__(self):
        return self.title
