from pacotedoprojeto.interface import *
from pacotedoprojeto.arquivo import *

arq = 'gestãoescolar.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    principal = menu_principal()
    if principal == 1:
        menupais = menu_pais()
        if menupais == 1:
            consultar_notas_aluno(arq)
    if principal == 2:
        professores = menu_professores()
        if professores == 1:
            consultar_notas_aluno(arq)
        elif professores == 2:
            cadastrar_novo_aluno(arq)