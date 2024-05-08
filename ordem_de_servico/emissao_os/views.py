from django.shortcuts import render
# views.py

# emissao_os/views.py

from django.http import HttpResponse
from django.views.generic import View
from .resources import OrdemServicoResource  # Corrigido o caminho de importação

class ExportOrdemServico(View):
    def get(self, request, *args, **kwargs):
        ordem_servico_resource = OrdemServicoResource()
        dataset = ordem_servico_resource.export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="ordens_de_servico.csv"'
        return response
