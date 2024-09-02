INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

numero = int(input("Informe um número: "))

if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

import json

# Exemplo de dados de faturamento diário
faturamento_json = '''
{
    "faturamento": [22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0, 
                    42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 0.0, 0.0, 
                    3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 0.0, 
                    35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 
                    0.0, 0.0, 25681.8318, 1718.1221, 0.0]
}
'''

faturamento = json.loads(faturamento_json)["faturamento"]

# Removendo dias sem faturamento
faturamento = [valor for valor in faturamento if valor > 0]

menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)
dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)

print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento_por_estado.values())

for estado, valor in faturamento_por_estado.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")


def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

string = input("Informe uma string: ")
print(f"String invertida: {inverter_string(string)}")
