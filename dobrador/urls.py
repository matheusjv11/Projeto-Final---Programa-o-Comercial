from django.urls import include, path
from dobrador.views import DobradorList

urlpatterns = [
    path('listar', DobradorList.as_view(), name='login'),
]