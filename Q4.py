dados = [{"estado": "SP", "valor": 67836.43}, {"estado": "RJ", "valor": 36678.66}, {"estado": "MG", "valor": 29229.88}, {"estado": "ES", "valor": 27165.48}, {"estado": "Outros", "valor": 19849.53}]

total = 0
for d in dados:
  total += d["valor"]

for d in dados:
  print(f'{d["estado"]}: {round(d["valor"] / total * 100, 2)}%')
