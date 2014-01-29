from django.db import models


class CodeExamples(models.Model):
    title = models.CharField(max_length=80)
    text = models.TextField()

    def __unicode__(self):
        return self.title
