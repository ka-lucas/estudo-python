#Crie uma função que receba uma lista de números e retorne o maior número.
def ordena(lista):
    length = len(lista)
    if(length == 0):
        return("lista vazia")
    else:
        return(sorted(lista))

    return soma

if __name__ == '__main__':
    entrada= []
    entrada = input("Entre com a lista separando por virgula\n")
    lista = [int(x) for x in entrada.split(",")]
    resultado = ordena(lista)
    print(f"resultado: {resultado}")
