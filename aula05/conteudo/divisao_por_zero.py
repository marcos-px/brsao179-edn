while True:
    try:
        numerador = int(input("Digite o numerador: "))
        while True:
            try:
                denominador = int(input("Digite o denominador: "))
                resultado = numerador / denominador
                print(f"O resultado é {resultado}")
                break
            except ZeroDivisionError:
                print("Erro! Não é possível dividir por zero.")

        break

    except ValueError:
        print("Digite um número.")

    finally:
        print("Tentando dividir...")

    
