def exibir_tabuada(numero):
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero_usuario = int(input("Digite um número inteiro para ver a tabuada: "))

exibir_tabuada(numero_usuario)