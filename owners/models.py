from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Owner(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Nome Proprietário:"))
    doc_number = models.CharField(max_length=18, verbose_name=_("CPF / CNPJ:"))
    phone_number = models.CharField(max_length=11, verbose_name=_("Celular/Telefone:"))
    email = models.CharField(max_length=100, verbose_name=_("E-mail do Proprietario:"))

    class Meta:
        ordering = ['name']
        verbose_name = _('Lista de proprietário')
        verbose_name_plural = _('Lista de proprietários')

    def __str__(self):
        return self.name
