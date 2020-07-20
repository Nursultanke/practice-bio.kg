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


class Statistic(models.Model):
    number = models.CharField(max_length=50, verbose_name="Число сел или городов")
    places = models.CharField(max_length=150, verbose_name="Где")
    issues = models.TextField(verbose_name="Что произошло?")

    class Meta:
        verbose_name = _("Стадистика выполняемых работ")
        verbose_name_plural = _("Список статистики")

    def __str__(self):
        return self.places
