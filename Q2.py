def fibo (n):
  if n == 1:
    return 0
  elif n == 2:
    return 1
  elif n <= 0:
    return "Numero invalido"
  else:
    return fibo(n-1)+fibo(n-2)

def teste_fibo(num):
  i = 1
  f = fibo(i)
  while f <= num:
    if f == num:
      return True
    i += 1
    f = fibo(i)
  return False

  
