from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Vehicle(models.Model):
    owner = models.ForeignKey('owners.Owner', verbose_name=_('Prosprietário:'), on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=256, verbose_name=_('Tipo do Veículo:'))
    vehicle_model = models.CharField(max_length=256, verbose_name=_('Modelo do veículo:'))
    doc_number = models.CharField(max_length=256, verbose_name=_('Chassi do veículo:'))

    class Meta:
        ordering = ['owner']
        verbose_name = _('Veículo')
        verbose_name_plural = _('Lista de Veículos')

    def __str__(self):
        return self.vehicle_model
