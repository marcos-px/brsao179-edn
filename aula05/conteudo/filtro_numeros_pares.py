print("Digite 5 números (irei mostrar apenas os ímpares): ")
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))

    if numero % 2 == 0: #condicação para ser par
        print(f"   {numero} é par - Pulando...!")
        continue

    print(f"     {numero} é impar!")