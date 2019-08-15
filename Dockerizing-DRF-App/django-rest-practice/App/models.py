from django.db import models


# Create your models here.
class Project(models.Model):
    """
    The database model to hold Project data
    fields: title, description
    """
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
