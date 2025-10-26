# 07 - Tratamento de Erros (Try / Except)
# Permite lidar com erros sem interromper o programa.

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")
