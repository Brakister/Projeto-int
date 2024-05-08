# emissao_os/resources.py

from import_export import resources
from .models import OrdemServico

class OrdemServicoResource(resources.ModelResource):
    class Meta:
        model = OrdemServico
