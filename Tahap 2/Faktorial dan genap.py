def faktorial(n):
  if n < 0:
    raise ValueError ("faktorial tdk terdefinisi")

  hasil = 1
  for i in range(1, n+1):
    hasil *= i
  return hasil

def genap(batas):
  hasil = 0
  for i in range (1, batas + 1):
    if i % 2 == 0:
      hasil += i
  return hasil

print (genap(11))
