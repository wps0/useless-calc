from django.db import models
from django.utils import timezone


class CalculationHistoryEntry(models.Model):
    calculation = models.CharField(max_length=1024)
    date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return 'Calculation({0})'.format(self.calculation)
