from rest_framework import viewsets, status
from rest_framework.response import Response

from escola.models import Aluno, Curso, Carro, Projeto
from escola.serializer import AlunoSerializer, CursoSerializer, CarroSerializer, ProjetoSerializer


# estamos criando duas classes de ViewSets usando o Django Rest Framework (DRF) para expor os modelos Aluno e Curso
# como uma API RESTful

# Uma ViewSet é uma classe do Django Rest Framework (DRF) que agrupa as ações CRUD relacionadas a um determinado
# modelo e as disponibiliza como endpoints de uma API REST.

# Aqui, estamos criando a classe AlunosViewSet, que herda de viewsets.ModelViewSet
# Isso indica que AlunosViewSet é uma classe de ViewSet do DRF que fornece automaticamente as ações CRUD (listar, criar,
# recuperar, atualizar e excluir) para o modelo Aluno.
class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""

    queryset = Aluno.objects.all()
    # O atributo queryset define o conjunto de objetos que serão disponibilizados pela ViewSet
    # Neste caso, estamos definindo o conjunto como todos os objetos do modelo Aluno (equivalente a SELECT * FROM Aluno)

    serializer_class = AlunoSerializer
    # O atributo serializer_class define o serializador que será usado para converter os objetos Aluno em JSON ou outros
    # formatos quando estiverem sendo retornados pela API. Aqui, estamos usando o AlunoSerializer para esse propósito.

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("aluno salvo")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CarroViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer


class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
# Com essas ViewSets, a API REST terá duas rotas para os modelos Aluno e Curso, com as ações CRUD devidamente
# configuradas e utilizando os serializadores AlunoSerializer e CursoSerializer para formatar os dados.
# Essas ViewSets tornam a criação de uma API para esses modelos simples e eficiente usando o Django Rest Framework.


