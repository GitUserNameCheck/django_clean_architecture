from django.db import models
# from clean_architecture.modules.infrastructure.db import Client, Location
from . import Client, Location


class Event(models.Model):
    id = models.BigAutoField(primary_key=True)
    location = models.ForeignKey(Location, models.DO_NOTHING)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    event_start = models.DateTimeField(blank=True, null=True)
    event_end = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'clean_architecture'
        managed = False
        db_table = 'event'

    def __str__(self):
	    return str(self.id) + ': ' + str(self.client) + "; " + str(self.location) + "; " + str(self.event_start) + "; " + str(self.event_end)
