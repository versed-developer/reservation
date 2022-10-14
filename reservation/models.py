import datetime
from django.db import models


class Rental(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    checkin = models.DateField(default=datetime.date.today)
    checkout = models.DateField()

    def __str__(self):
        return f'Res-{self.id}({self.checkin}, {self.checkout})'
