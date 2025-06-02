numero_secreto = 7
max_tentativas = 3


print(f"Tente adivinhar um número de 1 a 10!")
print(f"Você tem {max_tentativas} tentativas.")

for tentativa in range(1, max_tentativas + 1):
    while True:
        try:
            palpite = int(input(f"Tentativa: {tentativa}: "))

            if 1 <= palpite <= 10:
                break
            else: 
                print("Digite um número de 1 a 10! Não gastou tentativa!")
        except ValueError:
            print("Por favor, digite apenas números! Você não gastou uma tentativa!")
            
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número em ", tentativa, "tentativas")
        break
    elif palpite < numero_secreto:
        print("O número é MAIOR!")
    else:
        print("O número é MENOR!")

    if tentativa == max_tentativas:
        print(f"Suas tentativas acabaram, o número era {numero_secreto}")