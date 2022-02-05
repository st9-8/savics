"""savics_recruitement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core.views import home
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title='Savics Recruitment API',
        default_version='v1',
        description='All API endpoints documentation for EMR App.',
        terms_of_service='',
        contact=openapi.Contact(email='stephanefedim@gmail.com'),
    ),
    public=True,
    permission_classes=(AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/1.0/emr/', include('core.urls', namespace='emr')),
    path('swagger/', schema_view.with_ui('swagger'), name='swagger-ui'),
    path('home/', home, name='home')
]
