print('Sistema de Gestão Escolar!')
print('Selecione uma opção (selecione um número):')
print('1 - Pais')
print('2 - Professores')
while True:
    try:
        escolha = int(input('Sua escolha: '))
        if escolha not in [1, 2]:
            print ('Erro! Escolha 1 ou 2.')
        else:
            break
    except:
        print ('Por favor, escolha apenas um número')
while True:
    try:
        if escolha == 1:
            print('--'*30)
            print('Seja bem-vindo, Mãe/Pai!')
            print('Selecione uma opção (selecione um número):')
            print('1 - Consultar Notas de um Aluno:')
            escolha2 = int(input('Sua escolha: '))
            if escolha2 not in [1]:
                print('Por favor, selecione 1 ou ')
            else:
                break
    except:
        print('Por favor, escolha apenas um número')
