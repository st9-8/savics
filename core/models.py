from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

SEX = (
    ('Male', _('Male')),
    ('Female', _('Female'))
)

DIABETES = (
    ('Yes', _('Yes')),
    ('No', _('No')),
    ('Unknown', _('Unknown'))
)


def validate_positive_age(age):
    if age < 0:
        raise ValidationError(_('You can not enter a negative age'))


class Country(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class MedicalRecord(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    sex = models.CharField(max_length=6, choices=SEX)
    age = models.IntegerField(validators=[validate_positive_age])
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name='medical_records')
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, related_name='medical_records')
    with_diabetes = models.CharField(max_length=7, choices=DIABETES)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
