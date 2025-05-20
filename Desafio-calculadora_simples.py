
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    else:
        return a / b

def calculadora():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro! Por favor, insira um número válido.")
        return
    
    operacao = input("Escolha a operação (+, -, *, /): ")

    if operacao == "+":
        resultado = somar(num1, num2)
        print(f"O resultado da soma é: {resultado}")
    elif operacao == "-":
        resultado = subtrair(num1, num2)
        print(f"O resultado da subtração é: {resultado}")
    elif operacao == "*":
        resultado = multiplicar(num1, num2)
        print(f"O resultado da multiplicação é: {resultado}")
    elif operacao == "/":
        resultado = dividir(num1, num2)
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Operação inválida! Por favor, escolha uma operação válida.")

if __name__ == "__main__":
    calculadora()