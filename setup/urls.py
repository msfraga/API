from django.contrib import admin
from django.urls import path, include
# path = é usada para definir URLs
# include =  é usada para incluir outras configurações de URLs de outros arquivos na configuração principal
from escola.views import AlunosViewSet, CursosViewSet, CarroViewSet, ProjetoViewSet
# Esses ViewSets são responsáveis por manipular as operações CRUD para os modelos
from rest_framework import routers

router = routers.DefaultRouter()
# O DefaultRouter é usado para gerar automaticamente rotas para as ações CRUD padrão de um ViewSet.

router.register('alunos', AlunosViewSet, basename='Alunos')
# Esta linha registra o AlunosViewSet com o router
# Isso significa que o router irá gerar automaticamente as URLs para as ações CRUD do AlunosViewSet
# O primeiro argumento ('alunos') é o prefixo da URL que será adicionado às URLs geradas para o ViewSet
# Portanto, as URLs geradas para o ViewSet AlunosViewSet serão algo como /alunos/, /alunos/<pk>/, etc.
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('carros', CarroViewSet, basename='Carros')
router.register('projetos', ProjetoViewSet, basename='Projetos')

# Essas urlpatterns são usadas para mapear URLs a funções ou ViewSets
urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta linha define a URL para a interface de administração do Django, que geralmente é acessada em /admin/.
    path('', include(router.urls))
    # Esta linha define a URL raiz da nossa aplicação
    # inclui as URLs geradas pelo router nas urlpatterns da nossa aplicação

    # Dessa forma, todas as URLs geradas para os ViewSets AlunosViewSet e CursosViewSet serão adicionadas à
    # URL principal da nossa aplicação
]
