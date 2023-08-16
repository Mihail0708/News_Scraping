from django.db import models


class News(models.Model):
    title = models.CharField(max_length=300)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()

    def __str__(self):
        return self.title
