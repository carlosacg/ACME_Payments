from django.db import models
from django.utils.translation import gettext_lazy as _

class Day(models.Model):
    code = models.CharField(max_length=2, blank=False, null=False)
    name = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self) -> str:
        return f"{self.code}: {self.name}"

    class Meta:
        verbose_name = _('Day')
        verbose_name_plural = _('Days')

class Schedule(models.Model):
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)

    def __str__(self) -> str:
        return f"from: {self.start_time.strftime('%H:%M')} to: {self.end_time.strftime('%H:%M')}"

    class Meta:
        verbose_name = _('Schedule')
        verbose_name_plural = _('Schedules')

class Rate(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE, verbose_name=_('Day'))
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, verbose_name=_('Schedule'))
    price_by_hour = models.FloatField(default=0, verbose_name=_('Price'))
    quantity_hours = models.IntegerField(null=False, blank=False, verbose_name=_('Quantity hours'))
    total_price = models.FloatField(default=0, verbose_name=_('Total price'))

    class Meta:
        verbose_name = _('Rate')
        verbose_name_plural = _('Rates')

        # MO10:00-12:00, 30
        # TU10:00-12:00, 30
        # TH01:00-03:00, 50
        # SA14:00-18:00, 80
        # SU20:00-21:00  25

        # 215

