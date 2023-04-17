"""
URL configuration for tna project.
"""
from django.contrib import admin
from django.urls import path, include
from challenge.views import TNADataDetailView, TNARecordListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('challenge.urls')),
]
