nome_usuario = "Beatriz"
idade_atual = 15
carrinho_de_compras = ["livro", "caneta", "caderno"]

def calcular_descontos(valor_original, percentual_desconto):

    desconto = valor_original * (percentual_desconto / 100)
    valor_com_desconto = valor_original - desconto
    return valor_com_desconto