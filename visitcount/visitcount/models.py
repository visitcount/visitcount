from django.db import models


class Item(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class ItemView(models.Model):

    item = models.ForeignKey(Item)
    user_uid = models.CharField(max_length=100)

    class Meta:
        index_together = ['item', 'user_uid']