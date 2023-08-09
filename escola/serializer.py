from rest_framework import serializers, status
from rest_framework.response import Response

from escola.models import Aluno, Curso, Carro, Projeto


# Aqui, estamos definindo a classe AlunoSerializer
# Ela herda da classe serializers.ModelSerializer, que é uma classe de serializador do DRF usada para serializar
# modelos do Django
class AlunoSerializer(serializers.ModelSerializer):
    # A classe Meta é usada para fornecer metadados para o serializador
    # Neste caso, estamos definindo o modelo que será serializado e os campos que queremos incluir na serialização
    class Meta:
        # model = Aluno: Aqui, definimos o modelo que será serializado, que é o modelo Aluno
        model = Aluno
        #fields = ['id', 'nome', 'cpf', 'data_nascimento']
        # Com fields = '__all__', estamos incluindo todos os campos do modelo Aluno na serialização
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'


class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'


# Esses serializadores nos permitem converter objetos do Django (instâncias de Aluno e Curso) em JSON ou outros formatos
# compatíveis com a API REST. Isso é útil ao expor dados através de uma API, pois nos permite controlar quais campos dos
# modelos são expostos e como eles são formatados.