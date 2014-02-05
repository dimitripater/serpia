from django.db import models


class CodeExamples(models.Model):
    title = models.CharField(max_length=80)
    text = models.TextField()
    slug = models.SlugField()
    image = models.ImageField(upload_to='image', blank=True, null=True)

    def __str__(self):
        return self.title
