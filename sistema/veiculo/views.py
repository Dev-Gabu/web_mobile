from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse, Http404
from django.shortcuts import render
from django.views.generic import View
from veiculo.models import Veiculo

class ListarVeiculos(View):

    def get(self, request):
        contexto = {
            'veiculos' : Veiculo.objects.all().order_by('marca')
        }

        return render(request, 'veiculo/listar.html', contexto)
    
class FotoVeiculo(View):

    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
             raise Http404("Foto não encontrada ou arquivo não autorizado")
        except Exception as exception:
             raise exception
        return 0