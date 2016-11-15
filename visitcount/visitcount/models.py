from django.db import models


class Item(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title