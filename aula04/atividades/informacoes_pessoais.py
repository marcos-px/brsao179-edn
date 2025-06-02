print("===PROGRAMA DE INFORMAÇÕES PESSOAIS===")
print()

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
altura = float(input("Digite a sua altura :"))

print("\n--- PROCESSANDO INFORMAÇÕES ---")

#Quantos anos vou ter ano que vem?

proxima_idade = idade + 1

#Qual a minha altura em centímetros?

altura_cm = altura * 100

#Classificador de Idade

if idade < 2:
    classificador = "Bebê"
elif idade < 12:
    classificador = "Criança"
elif idade < 18:
    classificador = "Adolescente"
elif idade < 60:
    classificador = "Adulto"
else:
    classificador = "Idoso"

print("\n=== SEUS DADOS ===")

print("Nome :" + nome)

print("Idade atual: ", idade, "anos")

print(f"Altura: {altura:.2f} metros ({altura_cm:.0f} cm)")

print(f"No próximo ano você terá {proxima_idade} anos")

print(f"Categoria: {classificador}")

print("\n Programa finalizado com sucesso")