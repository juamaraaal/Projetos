import math

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro"

def potenciacao(base, expoente):
    return base ** expoente

def radiciacao(numero, indice):
    raiz = math.pow(numero, 1 / indice)
    return raiz

print("Selecione a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potenciação")
print("6 - Radiciciação")

operacao = int(input("Digite o número da operação desejada: "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado = 0

if operacao == 1:
    resultado = adicao(num1, num2)
elif operacao == 2:
    resultado = subtracao(num1, num2)
elif operacao == 3:
    resultado = multiplicacao(num1, num2)
elif operacao == 4:
    resultado = divisao(num1, num2)
elif operacao == 5:
    resultado = potenciacao(num1, num2)
elif operacao == 6:
    resultado = radiciacao(num1, num2)
else:
    print("Opção inválida!")

print("O resultado da operação é:", resultado)