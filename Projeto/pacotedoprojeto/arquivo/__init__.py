def arquivoExiste(nomedoarquivo):
    try:
        a = open(nomedoarquivo, 'rt')
    except:
        return False
    else:
        return True
    finally:
        a.close()

def criarArquivo(nomedoarquivo):
    try:
        a = open(nomedoarquivo, 'wt+')
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nomedoarquivo} criado com sucesso!')
    finally:
        a.close()