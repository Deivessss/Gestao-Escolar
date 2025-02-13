def menu_principal():
    print('-'*42)
    print(f'{'Sistema de Gestão Escolar!'.center(42)}')
    print('-' * 42)
    print('Selecione uma opção (selecione um número):')
    print('1 - Portal dos Pais')
    print('2 - Portal dos Professores')
    print('3 - Sair do Sistema')
    while True:
        try:
            escolha = int(input('Sua escolha: '))
            if escolha not in [1, 2, 3]:
                print ('Erro! Escolha 1, 2 ou 3.')
            else:
                return escolha
        except:
            print ('Por favor, digite um número inteiro válido (Suas opções são 1, 2 e 3)')

def menu_pais():
    while True:
        try:
            print('-'*42)
            print(f'{'Seja bem-vindo, Mãe/Pai!'.center(42)}')
            print('-' * 42)
            print('1 - Consultar Notas de um Aluno:')
            escolha = int(input('Sua escolha: '))
            if escolha not in [1]:
                print('Por favor, selecione 1 ')
            else:
                return escolha
        except:
            print('Por favor, digite um número inteiro válido')

def consultar_notas_aluno(nomearquivo):
    try:
        print('-'*30)
        print('Consultar notas de um aluno:')
        print('-' * 30)
        matricula = int(input('Digite a matrícula do aluno que deseja consultar: '))

        with open(nomearquivo, 'r') as a:
            for linha in a:
                dados = linha.split(';')
                if len(dados) < 2:
                    print('Erro: linha inválida no arquivo.')
                    continue

                if int(dados[0]) == matricula:
                    print(f'Aluno encontrado! Segue as notas do aluno: {dados[1]}')
                    return

        print('Aluno não encontrado.')

    except FileNotFoundError:
        print('Erro: arquivo não encontrado.')
    except ValueError:
        print('Erro: matrícula inválida.')
    except Exception as e:
        print(f'Erro: {e}')


def menu_professores():
    while True:
        try:
            print('-'*30)
            print('Seja bem-vindo, Professor/Professora!')
            matricula = int(input('Digite a matrícula do aluno que deseja modificar: '))
        except:
            print('Por favor, digite uma matrícula válida.')