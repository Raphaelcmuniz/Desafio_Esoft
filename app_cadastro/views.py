from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from .models import UserForm, User
import requests


def tela_listagem(request):
    context = {}
    users = User.objects.all()
    ordered_users = users.order_by("nome", "sobrenome")
    context["users"] = ordered_users

    return render(request, "listagem.html", context=context)


def tela_cadastro(request):
    context = {}

    gerador_url = "http://gerador-nomes.herokuapp.com/nome/aleatorio"
    gerador_response = requests.get(gerador_url)
    nome_aleatorio = gerador_response.json()

    form_data = User().__dict__

    form_data["nome"] = nome_aleatorio[0]
    form_data["sobrenome"] = nome_aleatorio[1] + " " + nome_aleatorio[2]

    form = UserForm(initial=form_data)

    context["form"] = form

    return render(request, "cadastro.html", context=context)


def tela_editar(request, user_id):
    context = {}
    user = User.objects.get(id=user_id)
    form = UserForm(user.__dict__)
    context["form"] = form
    context["user_id"] = user_id

    return render(request, "editar.html", context=context)


def editar_usuario(request, user_id):

    update_data = request.POST

    if not user_id:
        return HttpResponseBadRequest(content="user_id não enviado.")

    user = User.objects.get(id=user_id)

    for key, value in update_data.items():
        setattr(user, key, value)

    user.save()

    if not user.id:
        return HttpResponseBadRequest(content="erro. usuário não editado.")

    return redirect("/listagem")


def cadastrar_usuario(request):

    form = UserForm(request.POST)

    if not form.is_valid():
        return HttpResponseBadRequest(content="form contém erros.")

    new_user = form.save()

    if not new_user.id:
        return HttpResponseBadRequest(content="erro. usuário não cadastrado.")

    return redirect("/listagem")


def remover_usuario(request, user_id):

    if not user_id:
        return HttpResponseBadRequest(content="user_id precisa ser enviado.")

    user = User.objects.get(id=user_id)

    if user:
        user.delete()
        return HttpResponse(content="Usuário removido com sucesso")
    else:
        return HttpResponse(content="Usuário não encontrado")
