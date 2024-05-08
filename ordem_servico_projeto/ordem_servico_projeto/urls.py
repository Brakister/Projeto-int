from django.urls import path
from django.views.generic import RedirectView
from ordem_servico import views as ordem_servico_views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='criar_ordem_servico'), name='index'),
    path('criar_ordem_servico/', ordem_servico_views.criar_ordem_servico, name='criar_ordem_servico'),
    # Adicione outras URLs conforme necessário
]
