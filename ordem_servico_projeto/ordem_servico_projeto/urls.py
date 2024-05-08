from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from ordem_servico import views as ordem_servico_views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='criar_ordem_servico'), name='index'),
    path('criar_ordem_servico/', ordem_servico_views.criar_ordem_servico, name='criar_ordem_servico'),
    path('admin/', admin.site.urls),  # Adiciona as URLs do painel de administração
    # Adicione outras URLs conforme necessário
]
