from django.db import models
from django.utils import timezone


class Mileage(models.Model):
    id = models.AutoField(primary_key=True)

    stu_name = models.CharField(max_length=16, null=True)
    tel = models.CharField(max_length=16, null=True)
    gender = models.CharField(max_length=2, null=True)
    birth = models.DateField(blank=True, null=True)

    mileage = models.IntegerField()

    saving_date = models.DateTimeField(
            blank=True, null=True)
    using_date = models.DateTimeField(
        blank=True, null=True)

    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.stu_name


