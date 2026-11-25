import string 


masukan = input("masukan kata: ").lower()

for tanda_baca in string.punctuation:
  masukan = masukan.replace(tanda_baca, "")
daftar_kata = masukan.split()

frekuensi_kata = {}
for kata in daftar_kata:
    if kata in frekuensi_kata:
        frekuensi_kata[kata] += 1
    else:
        frekuensi_kata[kata] = 1

print("\nFrekuensi kemunculan kata:")
for kata, jumlah in frekuensi_kata.items():
    print(f"- {kata}: {jumlah}")