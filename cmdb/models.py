from django.db import models

# Create your models here.

class Business(models.Model):
    caption = models.CharField(max_length=32)

class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32,db_index=True)
    ip = models.GenericIPAddressField(db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey(to="Business", to_field='id',on_delete=models.DO_NOTHING)

