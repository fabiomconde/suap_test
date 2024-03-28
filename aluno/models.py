from django.db import models

from alunoplus.models import DocumentoTextoPlus

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class DocumentoTexto(DocumentoTextoPlus):

    identificador = models.CharField('Identificador do Documento', max_length=100, blank=True, null=False, db_index=True)

    def __str__(self):
        return f"{self.identificador}"

    def get_pdf(self):
        return "Original get_pdf"


#comentado para testar o command testar_plus
#se aprovado, utilizar
#from .metodo_custom import *