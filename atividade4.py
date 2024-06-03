def calcular_idade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento

def main():
    ano_atual = 2022
    while True:
        try:
            nome_completo = input("Digite seu nome completo: ")
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if not (1922 <= ano_nascimento <= 2021):
                raise ValueError("Ano fora do intervalo permitido.")
            idade = calcular_idade(ano_nascimento, ano_atual)
            print(f"Olá, {nome_completo}! Você completou ou completará {idade} anos em 2022.")
            break
        except ValueError as e:
            print(f"Erro: {e}. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
