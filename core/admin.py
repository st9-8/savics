from django.contrib import admin
from core.models import City, Country, MedicalRecord

admin.site.register(City)
admin.site.register(Country)
admin.site.register(MedicalRecord)