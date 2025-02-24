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


def menu_professores():
    while True:
        try:
            print('-'*42)
            print(f'{'Seja bem-vindo, Professor/Professora!'.center(42)}')
            print('-' * 42)
            print('1 - Consultar Notas de um aluno')
            print('2 - Cadastrar novo aluno.')
            escolha = int(input('Sua escolha: '))
            if escolha not in [1,2]:
                print('Erro! Escolha 1 ou 2')
            else:
                return escolha
        except:
            print('Erro! Digite um número inteiro válido.')



def consultar_notas_aluno(nomearquivo):
    try:
        print('-'*42)
        print(f'{'Consultar notas de um aluno:'.center(42)}')
        print('-' * 42)
        matricula = int(input('Digite a matrícula do aluno que deseja consultar: '))
        aluno_encontrado = False
        with open(nomearquivo, 'r') as a:
            for linha in a:
                dados = linha.split(';')
                if int(dados[0]) == matricula:
                    aluno_encontrado = True
                    print('-' * 30)
                    print(f'Aluno: {dados[1]}')
                    print(f'Idade: {dados[2]}')
                    print('Notas:')
                    print(f'Português: {dados[3]}')
                    print(f'Matemática: {dados[4]}')
                    print(f'Geografia: {dados[5]}')
                    print(f'História: {dados[6]}')
                    print(f'Educação Física: {dados[7]}')
        if not aluno_encontrado:
            print('Erro! Não há nenhum aluno com essa matrícula.')
    except Exception as e:
        print(f'Erro: {e}')

def cadastrar_novo_aluno(nomedoarquivo):
    print('-'*42)
    print(f'{'Cadastrar novo aluno'.center(42)}')
    print('-' * 42)

    #descobrindo qual é a última matricula.
    with open(nomedoarquivo, 'r') as a:
        for linha in a:
            matricula = int(linha.split(';')[0]) + 1
    try:
        nomedoaluno = input('Nome do aluno:').capitalize()
        idade = int(input('Idade: '))
        Português = int(input('Português: '))
        Matemática = int(input('Matemática: '))
        Geografia = int(input('Geografia: '))
        História = int(input('História: '))
        Educação_Física = int(input('Educação Física: '))
        with open(nomedoarquivo, 'a') as a:
            a.write(f'{matricula};{nomedoaluno};{idade};{Português};{Matemática};'
                    f'{Geografia};{História};{Educação_Física}\n')
    except Exception as erro:
        print(f'Erro: {erro}')
    else:
        print(f'Aluno {nomedoaluno} cadastrado com sucesso. Matrícula: {matricula}')
