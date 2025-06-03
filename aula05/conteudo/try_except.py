# Sem Tratamento

while True:
    try:
        numero = int(input("Digite um número: "))
        print("Número Válido!")
        break
    except ValueError:
        print("Número inválido")

