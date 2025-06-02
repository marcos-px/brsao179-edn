numero = int(input("Digite um número para ver a tabuada: "))

print(f"\nTabela do número {numero}")

for indice in range(1, 11):
    resultado = numero * indice
    print(f"{numero} x {indice} = {resultado}")
    
print("\n" + "="*40)
    #1 x 10 = 10
    #1 x 9 = 9

    

