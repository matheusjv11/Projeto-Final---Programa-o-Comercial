from django.views.generic import View 
from django.shortcuts import render
from django.http import HttpResponse
# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
import logging

logger = logging.getLogger(__name__)

class Login(View):

    def get(self, request):

        contexto = {
            'usuario':'',
            'senha':''
        }

        if request.user.is_authenticated:
            # Mudar para ir para a tela principal direto
            return render(request, 'autenticacao/login.html', contexto)

        return render(request, 'autenticacao/login.html', contexto)

    def post(self, request):

        # Armazena valores recebidos
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)

        #Apresenta no log (terminal) os valores recebidos
        logger.info('Usuários: {usuario}'.format(usuario=usuario))
        logger.info('Senha: {senha}'.format(senha=senha))

        user = authenticate(request, username=usuario, password=senha)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Usuário autenticado com sucesso')
            return render(request, 'autenticacao/login.html', {'mensagem':'Usuário inativo'})    
        return render(request, 'autenticacao/login.html', {'mensagem':'Usuário ou senha incorretos'}) 