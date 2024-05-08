from django.shortcuts import render, redirect
from .forms import OrdemServicoForm
from .models import EmissaoOrdemServico
import csv
from django.http import HttpResponse


def criar_ordem_servico(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            empresa = form.cleaned_data['loja']
            servico = form.cleaned_data['servico']
            data = form.cleaned_data['data']
            EmissaoOrdemServico.objects.create(empresa=empresa, servico=servico, data=data)
            return redirect('ordem_servico_confirmacao') # Redirecione para a página de confirmação
    else:
        form = OrdemServicoForm()
    return render(request, 'ordem_servico/criar_ordem_servico.html', {'form': form})

def ordem_servico_confirmacao(request):
    return render(request, 'ordem_servico/ordem_servico_confirmacao.html')

def historico_ordem_servico(request):
    ordens_servico = EmissaoOrdemServico.objects.all()
    return render(request, 'ordem_servico/historico_ordem_servico.html', {'ordens_servico': ordens_servico})

def emitir_planilha(request, mes, ano):
    # Consulte as emissões de ordem de serviço para o mês e ano especificados
    emissao_ordens_servico = EmissaoOrdemServico.objects.filter(data__month=mes, data__year=ano)

    # Crie uma resposta HTTP com o conteúdo da planilha
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="ordens_servico_{mes}_{ano}.csv"'

    # Crie um escritor CSV e escreva os dados das ordens de serviço
    writer = csv.writer(response)
    writer.writerow(['Empresa', 'Serviço', 'Produto', 'Data'])
    for emissao in emissao_ordens_servico:
        writer.writerow([emissao.empresa, emissao.servico, emissao.produto, emissao.data])

    return response

