from django.db import models

# Create your models here.
class AlunoPlus(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    plus = models.CharField(max_length=20)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome




class DocumentoTextoPlus(models.Model):

    data_Plus = models.DateTimeField('Data de Plus', blank=True, null=True)
    class Meta:
        abstract=True

    def novo_plus(self):
        return "Novo plus"
    
    def get_pdf(self):
        return "Alterar pelo plus"
