from django.views.generic import View
from django.shortcuts import render

class Login(View):

    def get(self, request):
        contexto = {'mensagem':'login'}
        return render(request,'autenticacao.html', contexto)