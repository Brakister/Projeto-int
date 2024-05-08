from django.shortcuts import render
from .forms import OrdemServicoForm

def criar_ordem_servico(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            # Processar o formulário aqui
            # Aqui você pode acessar os dados do formulário usando form.cleaned_data
            # e criar a ordem de serviço no banco de dados
            return render(request, 'ordem_servico/ordem_servico_confirmacao.html')
    else:
        form = OrdemServicoForm()
    return render(request, 'ordem_servico/criar_ordem_servico.html', {'form': form})
