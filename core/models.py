from django.db import models


UNIT_CHOICES = (
    (1, 'Kg'),
    (2, 'Lb'),
    (3, 'Item'),
    (4, 'Liter')
    )


class GroceryItem(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField()
    unit = models.IntegerField(choices=UNIT_CHOICES)
    favorit = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


class List(models.Model):
    crated = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.crated)


class ListItem(models.Model):
    grocery = models.ForeignKey(GroceryItem)
    purchased = models.BooleanField(default=False)
    root_list = models.ForeignKey(List)
    items = models.PositiveIntegerField(default=1)

    def __unicode__(self):
        return '%s in list for: %s' %\
            (self.grocery.title, self.root_list.crated)

    class Meta:
        ordering = ['-id']
