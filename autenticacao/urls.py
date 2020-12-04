from django.urls import include, path
from autenticacao.views import Login, Logout

app_name = "autenticacao"

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
]