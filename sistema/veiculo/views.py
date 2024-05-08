from django.shortcuts import render
from django.views.generic import View
from veiculo.models import Veiculo

class ListarVeiculos(View):

    def get(self, request):
        contexto = {
            'veiculos' : Veiculo.objects.all().order_by('marca')
        }

        return render(request, 'veiculo/listar.html', contexto)