from django.db import models
from imagekit.models import ProcessedImageField

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='portfolio/images',
        format='JPEG',
        options={'quality' : 100},
        blank=True,
        null=True
        )
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
