def hitung_nilai():
  try:
    nilai = int(input("masukan nilai anda: "))
  except:
    print ("masukan nilai yg benar")
    hitung_nilai()
  
  
  if 80 <= nilai <= 100:
    print ("A")
  elif 75 <= nilai <= 84:
    print ("B")
  elif 60 <= nilai <= 74:
    print ("C")
  elif 0 <= nilai <= 59:
    print ("D")
  else:
    print ("masukan yg benar, 0 - 100")

hitung_nilai()
  
    