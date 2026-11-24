print("======================================\n")
print("selamat datang di pembagi tagihan\n")
print("======================================\t")

try:
  tagihan = int(input("brp tagihannya: "))
  jumlahorang = int(input("brp yg patungan: "))
  persenlayanan = int(input("brp persen layanannya: "))

except:
  print ("masukan yg benar")
  exit()

nominallayanan = tagihan * (persenlayanan / 100)
total = tagihan + nominallayanan
totalpatungan = total / jumlahorang

print (f"""
hasil
tagihan: {tagihan:,.0f}RP
layanan: {persenlayanan}%
pembayaran per orang: {totalpatungan:,.0f}RP
""")
