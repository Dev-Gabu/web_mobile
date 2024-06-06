from django.urls import path
from veiculo.views import ListarVeiculos, FotoVeiculo, CriarVeiculos, EditarVeiculos, DeletarVeiculos, APIListarItens

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar-veiculos'),
    path('novo/', CriarVeiculos.as_view(), name = 'criar-veiculos'),
    path('api/', APIListarItens.as_view(),name='api-listar-veiculos'),
    path('<int:pk>/', EditarVeiculos.as_view(), name = 'editar-veiculos'),
    path('api/<int:pk>', APIDeletarVeiculos.as_view(),name='api-deletar-veiculos'),
    path('deletar/<int:pk>', DeletarVeiculos.as_view(), name = 'deletar-veiculos'),
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='foto-veiculo')
]