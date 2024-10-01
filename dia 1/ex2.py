#Escreva um programa que verifique se um número é par ou ímpar.
def impar(num):
    if(num%2 != 0):
        return("impar")
    else:
        return("par")
    return soma

if __name__ == '__main__':
    num = int(input("Entre com um numero\n"))
    resultado = impar(num)
    print(f"resultado: O numero {num} é {resultado}")
