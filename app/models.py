from django.db.models import Model


class Entry(Model):
    count = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.count)
