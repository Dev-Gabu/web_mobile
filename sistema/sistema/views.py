from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings


class Login(View):
    def get(self, request):
        contexto = {'mensagem':'login'}
        if request.user.is_authenticated:
            return HttpResponse('Usuário já está autenticado')
            #return redirect('/veiculos')
        else:
            return render(request,'autenticacao.html', contexto)
    
    def post(self,request):

        #Obtém as credenciais de autenticação do formulário
        usuario = request.POST.get('username',None)
        senha = request.POST.get('password',None)

        #Verifica as credenciais de autenticação fornecidas
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            #Verifica se o usuário ainda está ativo no sistema
            if user.is_active:
                login(request, user)
                return HttpResponse('Usuário autenticado com sucesso!')
                #return redirect("/veiculos")

            return render(request, "autenticacao.html", {'mensagem':'Usuário Inativo'})
        return render(request, "autenticacao.html", {'mensagem':'Usuário ou senha inválidos'})
    
class Logout(View):
    def get(self, request):
        logout(request)
        return request(settings.LOGIN_URL)