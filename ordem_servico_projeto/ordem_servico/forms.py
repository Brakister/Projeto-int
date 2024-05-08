from django import forms
from .models import Loja, Servico

class OrdemServicoForm(forms.Form):
    loja = forms.ModelChoiceField(queryset=Loja.objects.all())
    servicos = forms.ModelMultipleChoiceField(queryset=Servico.objects.all())
