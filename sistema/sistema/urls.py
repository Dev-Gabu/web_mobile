from django.contrib import admin
from django.urls import path, include
from sistema.views import Login, Logout

urlpatterns = [
    path('', Login.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('logout/', Logout.as_view(),name='logout'),
    path('veiculo/', include('veiculo.urls'), name='veiculos')
]
