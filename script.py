
Troque para a branch geracao-senhas.
Edite o arquivo script.py adicionando a seguinte lógica:
python
Copiar código
import random

def gerar_senha(comprimento, incluir_letras, incluir_numeros, incluir_simbolos):
    caracteres = ""
    if incluir_letras:
        caracteres += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if incluir_numeros:
        caracteres += "0123456789"
    if incluir_simbolos:
        caracteres += "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    if not caracteres:
        return "Erro: Nenhum tipo de caractere selecionado!"

    senha = "".join(random.choice(caracteres) for _ in range(comprimento))
    return senha
