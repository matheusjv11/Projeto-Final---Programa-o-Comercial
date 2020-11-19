from django.urls import include, path
from autenticacao.views import Login

urlpatterns = [
    path('', Login.as_view(), name='login'),
]