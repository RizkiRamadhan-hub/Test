print("======================================\n")
print("selamat datang di kalkulator sisa bagi\n")
print("======================================\t")

print("kalkulator sisa bagi adalah program yg dibuat utk mengonversi detik ke menit")

while True:
  try:
    masukan = int(input("masukan detik: "))
    menit = masukan // 60
    detik = masukan % 60
    print(f"hasil: {menit:,}:{detik:02d} menit")

  except ValueError:
    print("masukan angka desimal")
    break
  except:
    print ("error")

  lagi = input("apakah anda mau hitung lagi (y/n): ")
  if lagi.lower() == "y":
    pass
  else:
    print ("program selesai")
    break
  