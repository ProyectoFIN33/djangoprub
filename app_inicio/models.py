from django.db import models


class ProblemaAmbiental(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre 
    
class Problemasambientales(models.Model):
    nombre = models.CharField(max_length=100)
   
    descripcion = models.TextField()
    

    def __str__(self):
        return self.nombre