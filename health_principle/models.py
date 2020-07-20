from django.db import models
from django.utils.translation import ugettext_lazy as _


class HealthPrinciple(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    img = models.ImageField(upload_to='healthPrinciple/', null=True, blank=True, verbose_name="Иконки ")

    class Meta:
        verbose_name = _("Принципы здоровья")
        verbose_name_plural = _("Список принципов здоровья")

    def __str__(self):
        return self.title


