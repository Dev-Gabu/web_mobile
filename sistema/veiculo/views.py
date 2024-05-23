from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, Http404
from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from veiculo.models import Veiculo
from veiculo.serializers import SerializadorVeiculo
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from veiculo.forms import FormularioVeiculo
from django.urls import reverse_lazy

class ListarVeiculos(ListView):

    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

    def get_queryset(self, **kwargs):
        queryset =  Veiculo.objects.all()
        pesquisa = self.request.GET.get('pesquisa', None)
        if pesquisa is not None:
            query = queryset.filter(modelo_icontains=pesquisa)
        return queryset
    
class APIListarItens(ListAPIView):
    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
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
    
class CriarVeiculos(LoginRequiredMixin, CreateView):

    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')

class EditarVeiculos(LoginRequiredMixin, UpdateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')

class DeletarVeiculos(LoginRequiredMixin, DeleteView):
    model = Veiculo
    template_name = 'veiculo/deletar.html'
    success_url = reverse_lazy('listar-veiculos')