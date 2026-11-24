print("======================================\n")
print("selamat datang di konverter suhu celcius ke fahrenheit\n")
print("======================================\t")

while True:
  try:
    celcius = int(input("suhu celcius: "))
    fahrenheit = (celcius * 9/5) + 32
    print (f"hasil: {fahrenheit:.2f} fahrenheit")

    if celcius > 35:
      print ("suhu panas")
    elif 20 <= celcius <= 35:
      print ("suhu normal")
    else:
      print ("sejuk")
    
  
  except ValueError:
    print("masukan angka desimal")
    continue
  except:
    print ("error")

  lagi = input("apakah anda mau hitung lagi (y/n): ")
  if lagi.lower() == "y":
    pass
  else:
    print ("program selesai")
    break
  