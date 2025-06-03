"""
Se a senha tiver menos de 8 caracteres é considerada fraca. 
A senha será "12345678"
"""
print("Sistema de senha - digite sair para encerrar")

quantidade_caracteres = 8

while True:
    senha = input("Digite a senha (ou 'sair')")

    if senha.lower() == "sair":
        print("Tchau, tchau, encerrando o sistema...")
        break

    if len(senha) < quantidade_caracteres:
        print(f"Senha muito curta! Deve ter ao menos {quantidade_caracteres} caracteres")
        continue

    if senha == "12345678":
        print("Acesso Liberado")
        break
    else:
        print("Senha incorreta! Tente novamente!")