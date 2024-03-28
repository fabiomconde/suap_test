

import datetime
from django.core.management.base import BaseCommand

from aluno.models import DocumentoTexto

import warnings

# Desativa todos os avisos
warnings.filterwarnings('ignore')

class Command(BaseCommand):
    def handle(self, *args, **options):

        print("\nNovo ITEM _______________________")
        novo = DocumentoTexto()
        novo.identificador = 'Identificador 1'
        novo.data_Plus = datetime.datetime.now()
        novo.save()
        print(novo.identificador)
        print(novo.get_pdf())
        print(novo.novo_plus())        
        print(novo.data_Plus)

        print("\nBusca ITEM _______________________")
        busca = DocumentoTexto.objects.last()
        print(busca.identificador)
        print(busca.get_pdf())
        print(novo.novo_plus())
        print(busca.data_Plus)

        print("\nBusca MUDA VALOR _______________________")
        busca.identificador = 'Identificador Busca'
        busca.data_Plus = datetime.datetime.now()
        busca.save()
        print(busca.identificador)
        print(busca.get_pdf())
        print(novo.novo_plus())
        print(busca.data_Plus)

        print("\nImport metodo_custom")
        from aluno import metodo_custom
        print(novo.get_pdf())
        print(novo.novo_plus())

        print("\nBusca2 ITEM _______________________")
        busca2 = DocumentoTexto.objects.last()
        print(busca2.identificador)
        print(busca2.get_pdf())
        print(novo.novo_plus())
        print(busca2.data_Plus)

        print("\nBusca2 MUDA VALOR _______________________")
        busca2.identificador = 'Identificador Busca2'
        busca2.data_Plus = datetime.datetime.now()
        busca2.save()
        print(busca2.identificador)
        print(busca2.get_pdf())
        print(novo.novo_plus())
        print(busca2.data_Plus)        
        
        print("\nBusca3 ITEM _______________________")
        busca3 = DocumentoTexto.objects.last()
        print(busca3.identificador)
        print(busca3.get_pdf())
        print(novo.novo_plus())
        print(busca3.data_Plus)
        

