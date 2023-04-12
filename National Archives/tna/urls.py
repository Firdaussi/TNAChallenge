"""
URL configuration for tna project.
"""
from django.contrib import admin
from django.urls import path
from challenge.views import TNADataDetailView, TNARecordListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TNARecordListView.as_view(), name='tna_list_url'),
    path('<slug:pk>/', TNADataDetailView.as_view(), name="tna_detail_url"),
]
