from django.urls import path

from . import views

urlpatterns = [
    path("", views.tela_cadastro, name="cadastro"),
    path("listagem", views.tela_listagem, name="listagem"),
    path("editar/<str:user_id>", views.tela_editar, name="editar"),
    path("cadastrar_usuario", views.cadastrar_usuario, name="cadastrar_usuario"),
    path("editar_usuario/<str:user_id>", views.editar_usuario, name="editar_usuario"),
    path(
        "remover_usuario/<str:user_id>", views.remover_usuario, name="remover_usuario"
    ),
]
