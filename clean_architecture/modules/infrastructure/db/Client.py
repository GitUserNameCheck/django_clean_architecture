from django.db import models

class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=500, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)

    class Meta:
        app_label = 'clean_architecture'
        managed = False
        db_table = 'client'

    def __str__(self):
	    return str(self.id) + ': ' + self.name
