from pacotedoprojeto.interface import *
from pacotedoprojeto.arquivo import *

arq = 'gestãoescolar'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    principal = menu_principal()
    if principal == 1:
        menupais = menu_pais()
        if menupais == 1:
            consultar_notas_aluno(arq)