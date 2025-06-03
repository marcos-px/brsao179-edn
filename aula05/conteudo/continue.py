#Pulando Iteração

print("Mostrando números de 1 a 6 pulando o número 3:")
for i in range(1,9):
    if i == 8:
        print(f"Pulando o índice: {i}...")
        continue
    print(f"Número {i}")
