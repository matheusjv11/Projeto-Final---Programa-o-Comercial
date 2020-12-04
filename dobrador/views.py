from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from dobrador.models import Dobrador
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from dobrador.forms import FormularioDobrador
# Create your views here.

@method_decorator(login_required, name='dispatch')
class DobradorList(ListView):
    model = Dobrador
    context_object_name = "lista_dobradores"
    template_name = 'dobrador/listar.html'

@method_decorator(login_required, name='dispatch')
class DobradorNew(CreateView):
    
    model = Dobrador
    form_class = FormularioDobrador
    template_name = 'dobrador/novo.html'
    success_url = "/"    
    
@method_decorator(login_required, name='dispatch')
class DobradorEdit(UpdateView):
    
    model = Dobrador
    form_class = FormularioDobrador
    template_name = 'dobrador/editar.html'
    success_url = "/"

@method_decorator(login_required, name='dispatch')
class DobradorDelete(DeleteView):
    
    model = Dobrador
    template_name = 'dobrador/deletar.html'
    success_url = "/"