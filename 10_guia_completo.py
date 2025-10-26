# 10 - Guia Completo + Atalhos Extras

# ✅ Atalhos e funções úteis do Python:
# len() → retorna o tamanho (número de itens)
# type() → mostra o tipo do dado
# range() → gera uma sequência numérica
# enumerate() → gera índices e valores em um loop
# sum() → soma todos os elementos de uma lista
# max() / min() → retorna o maior/menor valor
# round() → arredonda número
# sorted() → ordena listas
# map() / filter() / lambda → funções funcionais avançadas

dados = [10, 20, 30, 40, 50]

print("Tamanho da lista:", len(dados))
print("Tipo da variável:", type(dados))
print("Soma dos valores:", sum(dados))
print("Maior valor:", max(dados))
print("Lista ordenada:", sorted(dados))

for i, valor in enumerate(dados):
    print(f"Índice {i} -> Valor {valor}")

print("Guia completo executado com sucesso!")
