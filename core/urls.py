from django.urls import path
from core.views import CreateListMedicalRecordView, ListMinorsMedicalRecordView

app_name = 'emr'

urlpatterns = [
    path('', CreateListMedicalRecordView.as_view(), name='emr_endpoint'),
    path('minors/', ListMinorsMedicalRecordView.as_view(), name='minors')
]
