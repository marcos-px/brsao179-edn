from funcao_simples import saudacao, linhas_separadoras
from funcao_cumprimentar import cumprimentar, cumprimentar_completo

# cumprimentar("Sandra")
# linhas_separadoras()
# saudacao()
# linhas_separadoras()

nome = input("Digite seu nome: ")
curso = input("Digite o nome do curso: ")

mensagem = cumprimentar_completo(nome, curso)
print(mensagem)