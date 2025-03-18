from django.db import models

from clean_architecture.modules.infrastructure.db import Event, ServiceEmployee

class EventServiceEmployee(models.Model):
    id = models.BigAutoField(primary_key=True)
    event = models.ForeignKey(Event, models.DO_NOTHING)
    service_employee = models.ForeignKey(ServiceEmployee, models.DO_NOTHING)

    class Meta:
        app_label = 'clean_architecture'
        managed = False
        db_table = 'event_service_employee'

    def __str__(self):
	    return str(self.id) + ': ' + str(self.event) + "; " + str(self.service_employee)
