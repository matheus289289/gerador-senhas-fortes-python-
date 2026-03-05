import random
import string

def gerar_senha(tamanho=12):
    caracteres = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Usuário define quantas senhas e o tamanho
quantidade = int(input("⚓Bem-vindo ao Gerador de Senhas⚓.\nQuantas senhas você deseja gerar?🤔 "))
tamanho = int(input("Quantos caracteres por senha?🤔 "))

# Gera e imprime
for i in range(quantidade):
    senha = gerar_senha(tamanho)
    print(f"Senha {i + 1}: {senha}")

input("\nPRESSIONE ENTER PARA SAIR...")