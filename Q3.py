#dados = [{"dia": 1, "valor": 22174.1664},{"dia": 2, "valor": 24537.6698},{"dia": 3, "valor": 26139.6134}, {"dia": 4, "valor": 0.0}]

import json

with open('dados.json') as f:
  dados = json.load(f)
  
valores = []
total = 0
for d in dados:
  if d["valor"] != 0.0:
    v = d["valor"]
    total += v
    valores.append(v)

media = total / len(valores)

val_med = valores
val_med.sort()

min = val_med[0]
max = val_med[-1]

print(f'Menor valor de faturamento: {min}')
print(f'Maior valor de faturamento: {max}')

val_med.append(media)
val_med.sort()

i = val_med.index(media)

sup_med = val_med[i+1:]

print(f'Número de dias com faturamento acima da média: {len(sup_med)}')
