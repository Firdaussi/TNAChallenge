from django.views.generic import DetailView, ListView
from django.http import Http404
from django.shortcuts import render
from challenge.models import TNARecord

class TNADataDetailView(DetailView):
    model = TNARecord
    template_name = 'challenge/record_detail.html'
    context_object_name = "tna_detail"

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset=queryset)
        except TNARecord.DoesNotExist:
            raise Http404("No record found")

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            context = {"message": "No record found."}
            return render(request, "challenge/message.html", context)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.object.title != None:
            context['chosenValue'] = self.object.title
            context['chosenType'] = 'title'
        elif self.object.description != None:
            context['chosenValue'] = self.object.description
            context['chosenType'] = 'description'
        elif self.object.citable != None:
            context['chosenValue'] = self.object.citable
            context['chosenType'] = 'citable'
        else:
            context['chosenValue'] = 'not sufficient information'
            context['chosenType'] = None

        return context

class TNARecordListView(ListView):
    model = TNARecord
    template_name = 'challenge/record_list.html'
    context_object_name = 'tna_list'

    def get_queryset(self):
        return TNARecord.objects.all()

