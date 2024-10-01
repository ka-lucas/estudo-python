#Crie um programa que solicite dois números do usuário e imprima a soma deles.
def soma():
    number1 = int(input("Digite o primeiro numero:\n"))
    number2 = int(input("Digite o segundo numero:\n"))
    soma = number1+number2
    return soma

if __name__ == '__main__':
    resultado = soma()
    print(f"A soma é: {resultado}")
