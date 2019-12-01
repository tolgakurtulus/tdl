from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render
from .models import ToDoList

# Create your views here.

class ToDoListListView(ListView):

    model = ToDoList
    paginate_by = 10  # if pagination is desired


class ToDoListDetailView(DetailView):

    model = ToDoList

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
