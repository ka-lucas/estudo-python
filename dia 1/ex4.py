#Implemente um programa que receba uma lista de palavras e ordene-as em ordem alfabética.
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
    lista = [x for x in entrada.split(",")]
    resultado = ordena(lista)
    print(f"resultado: {resultado}")
