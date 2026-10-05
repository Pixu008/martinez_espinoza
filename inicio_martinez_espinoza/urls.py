from django.urls import path
from . import views

app_name = 'inicio'

urlpatterns = [
    path('', views.index, name='index'),
    path('tema/<int:tema_id>/', views.detalle_tema, name='detalle'), # Ruta para la redirección
]