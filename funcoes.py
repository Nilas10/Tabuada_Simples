"""
-> As funções são bloco de código que realizam uma tarefa.
-> Esses códigos são reutilizaveis.
-> Ajudam a organizar o código.
-> Ajuda a não repetir códigos desnecessariamente.

"""
#Sintaxe (Escrita) da função:

def nome_funcao():
    """
    #Corpo da função
    #Comandos da função
    """
#def - Palavra chave para definir a funçõ
#nome_função() - Nome que identifica uma função

print("Função Simples")
def saudacao():
    print("Ola! Boa noite Ass: Bonner")
#precisamos chamar a função     
saudacao()

print(20*"-")
print("Função com parametros")

def saudacao_turma(nome_turma):
    print(f"Boa noite! {nome_turma} ")
saudacao_turma("2025.1 Top")
saudacao_turma("Galera")

print(20*"-")
print("Função com retorno")

def soma():
    return 1 + 2

print("O resultado é: ", soma())