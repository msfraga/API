from django.contrib import admin
from escola.models import Aluno, Curso, Carro

#  estamos registrando os modelos Aluno e Curso na interface de administração do Django e personalizando como eles serão
#  exibidos e manipulados na página de administração.

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

# Aqui, estamos registrando o modelo Aluno com a classe Alunos personalizada na
# página de administração. Isso fará com que o modelo Aluno seja exibido e possa ser editado na interface de
# administração do Django conforme as configurações definidas na classe Alunos.
admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)

admin.site.register(Curso, Cursos)


class Carros(admin.ModelAdmin):
    list_display = ('marca', 'ano', 'cor')
    list_display_links = ('marca',)
    search_fields = ('marca',)

admin.site.register(Carro, Carros)