"""
URL configuration for tna project.
"""
from django.urls import path
from challenge.views import TNADataDetailView, TNARecordListView

urlpatterns = [
    path('', TNARecordListView.as_view(), name='tna_list_url'),
    path('<slug:pk>/', TNADataDetailView.as_view(), name="tna_detail_url"),
]
