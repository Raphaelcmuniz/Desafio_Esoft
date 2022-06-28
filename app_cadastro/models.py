from django.db import models
import django.forms as forms

# Create your models here.
class User(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    email = models.CharField(max_length=200)
    apelido = models.CharField(max_length=100, blank=True)
    observacao = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.nome


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "nome",
            "sobrenome",
            "idade",
            "data_nascimento",
            "email",
            "apelido",
            "observacao",
        ]
        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "class": "form-control form-control-sm",
                    "maxlength": "100",
                }
            ),
            "sobrenome": forms.TextInput(
                attrs={
                    "class": "form-control form-control-sm",
                    "maxlength": "100",
                }
            ),
            "idade": forms.TextInput(
                attrs={
                    "class": "form-control form-control-sm",
                    "maxlength": "3",
                }
            ),
            "data_nascimento": forms.DateInput(
                attrs={
                    "class": "form-control form-control-sm",
                    "maxlength": "10",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control form-control-sm",
                    "maxlength": "50",
                }
            ),
            "apelido": forms.TextInput(
                attrs={"class": "form-control form-control-sm", "maxlength": "50"}
            ),
            "observacao": forms.Textarea(
                attrs={"class": "form-control form-control-sm", "maxlength": "300"}
            ),
        }
