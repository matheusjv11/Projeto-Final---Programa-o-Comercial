from django.urls import include, path
from dobrador.views import DobradorList, DobradorEdit, DobradorDelete, DobradorNew

app_name = "dobradores"

urlpatterns = [
    path('listar', DobradorList.as_view(), name='listar'),
    path("novo/", DobradorNew.as_view(), name="novo"),
    path("<int:pk>/", DobradorEdit.as_view(), name="editar"),
    path("excluir/<int:pk>/", DobradorDelete.as_view(), name="excluir"),
]