# Calculadora em Python utilizando operadores básicos: adição, subtração, multiplicação e divisão

executaCalculadora = True
opcaoEscolhida = 0
prosseguirNumeroNaoDivisivel = True
opcaoEscolhidaDivisao = 0

# Laço de repetição para executar a calculadora enquanto o usuário digitar algo diferente de 5
while executaCalculadora:
    print('-----CALCULADORA-----')
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('Pressione "5" para fechar a calculadora')
    print()
    # Se a opção selecionada == 5, então o laço de repetição recebe a condição False, então para a execução do código
    opcaoEscolhida = int(input('Selecione uma opção: '))
    if opcaoEscolhida == 5:
        executaCalculadora = False
        print('Calculadora encerrada.')
        # Se a opção selecionada for maior que 5, a opção não existe e retorna para o início do loop
    elif opcaoEscolhida > 5:
        print('A opção selecionada não existe!')
        print()
        continue
    # Opção 1 responsável por efetuar a soma dos digítos
    elif opcaoEscolhida == 1:
        numeroA = int(input('Digite o primeiro número: '))
        numeroB = int(input('Digite o segundo número: '))
        resultado = numeroA + numeroB
        print(f'O resultado da adição é {resultado}')
        print()
        continue
    # Opção 2 responsável pela subtração dos digítos
    elif opcaoEscolhida == 2:
        numeroA = int(input('Digite o primeiro número: '))
        numeroB = int(input('Digite o segundo número: '))
        resultado = numeroA - numeroB
        print(f'O resultado da subtração é {resultado}')
        print()
        continue
    # Opção 3 responsável pela multiplicação
    elif opcaoEscolhida == 3:
        numeroA = int(input('Digite o primeiro número: '))
        numeroB = int(input('Digite o segundo número: '))
        resultado = numeroA * numeroB
        print(f'O resultado da multiplicação é {resultado}')
        print()
        continue
    # Opção 4 responsável pela divisão
    elif opcaoEscolhida == 4:
        numeroA = int(input('Digite o primeiro número: '))
        numeroB = int(input('Digite o segundo número: '))
        print()
        # Verifica se o resto da divisão não é zero, pois dessa forma valida se o número A é divisível por B
        resto = numeroA % numeroB
        # Se o número obter resto diferente de zero, retornará a mensagem solicitando se quer realmente continuar com essa divisão
        if resto != 0:
            print(
                f'O número {numeroA} não é divisivel por {numeroB}, deseja prosseguir? ')
            print('1. Sim')
            print('2. Não')
            # Laço de repetição responsável por aguardar a resposta do usuário, se deseja ou não prosseguir com o cálculo
            while prosseguirNumeroNaoDivisivel:
                opcaoEscolhidaDivisao = int(input('Selecione uma opção: '))
                # Se a opçao selecionado for 1, "Sim", é retornado o resultado mesmo não sendo divisivel
                if opcaoEscolhidaDivisao == 1:
                    resultado = numeroA / numeroB
                    print(f'O resultado da divisão é {resultado}')
                    print()
                    break
                # Se a opcao for 2, quebra o laço e retorna para o início da calculadora
                elif opcaoEscolhidaDivisao == 2:
                    print()
                    break

                else:
                    print('A opção selecionada não existe! Tente novamente!')
                    continue
                # Se a divisão obter resto zero, já efetua a conta direto e retorna o resultado
        else:
            resultado = numeroA / numeroB
            print(f'O resultado da divisão é {resultado}')
            print()
            continue
