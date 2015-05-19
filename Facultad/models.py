from django.db import models

class Facultad(models.Model):
     codigo=models.CharField(primary_key=True,max_length=10)
     nombre=models.CharField(max_length=50)

     #devuelve el nombre de la facultad en el admin
     def __unicode__(self):
        return self.nombre

     class Meta:
        #nombre en plural del modelo en el admin
        verbose_name_plural='Facultades'
