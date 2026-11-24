print ("""
syarat username:
1. panjang minimal 5 karakter
2. panjang maksimal 15 karakter
3. tdk mengandung spasi\n
""")
uname = input("masukan username anda: ")

if len(uname) < 4 or len(uname) > 15 or " " in uname:
  print ("username tdk valid")
else:
  print ("username valid")
