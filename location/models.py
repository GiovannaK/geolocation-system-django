from django.db import models


class Location(models.Model):
    location = models.CharField(max_length=200, verbose_name="Localização")
    destination = models.CharField(max_length=200, verbose_name="Destino")
    distance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Distância")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")

    def __str__(self):
        return f'Distância entre {self.location} até {self.destination} é {self.distance} km'