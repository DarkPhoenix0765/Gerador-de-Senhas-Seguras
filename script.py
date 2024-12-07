def validar_entrada(valor, tipo):
    if tipo == "int":
        try:
            return int(valor)
        except ValueError:
            return "Erro: Digite um número válido."
    elif tipo == "bool":
        return valor.lower() in ["sim", "s", "yes", "y"]
