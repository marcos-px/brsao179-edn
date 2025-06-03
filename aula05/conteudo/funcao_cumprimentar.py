def cumprimentar(nome):
    """
    Função que cumprimenta uma pessoa pelo nome.
    
    Parâmetro
        nome(str): Nome da pessoa
    """

    mensagem = f"Olá, {nome}! Você está estudando Python!"
    print(mensagem)
    return mensagem

def cumprimentar_completo(nome, curso):
    """
    Função com múltiplos parâmetros

    Parâmetros:
        nome(str): Nome da pessoa
        curso(str): Nome do curso

    """
    
    # print(f"Olá, {nome}! Você está estudando {curso}!")
    return f"Olá, {nome}! Você está estudando {curso}!"

def dividir(numerador, denominador):

    try:
        resultado = numerador/denominador
        return resultado
        
    except Exception as e: #Exceção de função
        print(f"Deu erro {e}")
        return None