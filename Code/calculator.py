print("********** Bem vindo a Calculadora em Python **********")

print("Selecione a operação desejada:")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Digite sua opção (1/2/3/4): ")


def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

if operacao == "1":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = soma(num1,num2)
    print("O resultado da soma é: ", resultado)

elif operacao == "2":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = subtracao(num1,num2)
    print("O resultado da subtração é: ", resultado)

elif operacao == "3":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = multiplicacao(num1,num2)
    print("O resultado da multiplicação é: ", resultado)

elif operacao == "4":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = divisao(num1,num2)
    print("O resultado da divisão é: ", resultado)

else: print("Opção inválida! ")
    
    
    