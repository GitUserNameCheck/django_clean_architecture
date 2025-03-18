from django.db import models
from clean_architecture.modules.infrastructure.db import Employee, Service

class ServiceEmployee(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    service = models.ForeignKey(Service, models.DO_NOTHING)

    class Meta:
        app_label = 'clean_architecture'
        managed = False
        db_table = 'service_employee'

    def __str__(self):
	    return str(self.id) + ': ' + str(self.employee) + "; " + str(self.service)