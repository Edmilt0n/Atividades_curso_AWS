def calculator():
    while True:
        # Mostrar o menu de operações
        print("Selecione a operação:")
        print("1: Soma +")
        print("2: Subtração -")
        print("3: Multiplicação *")
        print("4: Divisão /")
        print("0: Sair")

        # Solicitar a operação do usuário
        choice = input("Digite o número da operação: ")

        # Verificar se o usuário deseja sair
        if choice == '0':
            print("Saindo...")
            break

        # Verificar se a escolha é válida
        if choice in ['1', '2', '3', '4']:
            # Solicitar os dois números ao usuário
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            # Realizar a operação selecionada
            if choice == '1':
                result = num1 + num2
                print(f"O resultado de {num1} + {num2} é: {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"O resultado de {num1} - {num2} é: {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"O resultado de {num1} * {num2} é: {result}")
            elif choice == '4':
                if num2 != 0:
                    result = num1 / num2
                    print(f"O resultado de {num1} / {num2} é: {result}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
        else:
            # Caso a escolha não seja válida, mostrar mensagem de erro
            print("Essa opção não existe")

# Chamar a função calculadora
calculator()
