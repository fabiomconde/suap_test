
from .models import DocumentoTexto
from alunoplus.models import DocumentoTextoPlus

DocumentoTexto.get_pdf = DocumentoTextoPlus.get_pdf
