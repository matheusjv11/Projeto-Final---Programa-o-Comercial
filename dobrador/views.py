from django.shortcuts import render
from django.views.generic import ListView, View
from dobrador.models import Dobrador
# Create your views here.

class DobradorList(ListView):
    model = Dobrador
    context_object_name = "lista_dobradores"
    template_name = 'dobrador/listar.html'
