from django.contrib import admin
from django.urls import path
from sistema.views import Login, Logout

urlpatterns = [
    path('', Login.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('logout', Logout.as_view(),name='logout')
]
