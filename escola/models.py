from django.db import models

# Os modelos representam tabelas do banco de dados e definem os campos que cada tabela deve conter

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    # Esse método é chamado quando precisamos converter um objeto Aluno em uma representação de string, geralmente usado
    # para fins de exibição. Neste caso, estamos retornando o atributo nome do objeto Aluno como representação de string
    def __str__(self):
        return self.nome


class Curso(models.Model):
    # Aqui, estamos definindo uma tupla de tuplas chamada NIVEL, que contém opções para o campo nivel.
    NIVEL = (('B', 'Básico'), ('I', 'Intermediário'), ('A', 'Avançado'))
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.descricao


class Carro(models.Model):
    marca = models.CharField(max_length=15, null=False)
    ano = models.DateField()
    cor = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.marca


class Projeto(models.Model):
    nome = models.CharField(max_length=15, null=False)
    departamento = models.CharField(max_length=15, null=False)
    inicio = models.DateField()
    fim = models.DateField()

    def __str__(self):
        return self.nome