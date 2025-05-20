"""
como criar um programa em python que peça ao usuário para digitar uma palavra. Em seguida,
crie uma função chamada inverter_palavra que recebe essa palavra como argumento e retorna
a palavra invertida. Por fim, exiba a palavra original e a palavra invertida.

"""

palavra = "senac"
inverter = palavra[::-1] #Inverter uma string
print(inverter)


def inverter_palavra(palavra):
    return palavra[::-1]

print(f"Palavra original: {palavra}")
print(f"Palavra invertida: {inverter}")
