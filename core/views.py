from rest_framework import generics
from django.contrib import messages
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from rest_framework.permissions import AllowAny
from core.serializers import MedicalRecordSerializer
from core.models import MedicalRecord, City, Country
from django.utils.translation import gettext_lazy as _


class CreateListMedicalRecordView(generics.ListCreateAPIView):
    queryset = MedicalRecord.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = MedicalRecordSerializer

    def create(self, request, *args, **kwargs):
        super(CreateListMedicalRecordView, self).create(request, *args, **kwargs)

        messages.success(request, _('You record has been created successfully'))
        return HttpResponseRedirect(redirect_to=reverse('home'))


class ListMinorsMedicalRecordView(generics.ListAPIView):
    queryset = MedicalRecord.objects.filter(age__lte=18)
    permission_classes = (AllowAny,)
    serializer_class = MedicalRecordSerializer


def home(request):
    countries = Country.objects.all()
    cities = City.objects.all()

    context = {
        'countries': countries,
        'cities': cities
    }
    return render(request, 'core/record_form.html', context)
