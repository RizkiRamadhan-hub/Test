print ("""
syarat username:
1. panjang minimal 5 karakter
2. panjang maksimal 15 karakter
3. tdk mengandung spasi\n
""")[span_1](start_span)[span_1](end_span)
uname = input("masukan username anda: ")[span_2](start_span)[span_2](end_span)

if len(uname) < 5 or len(uname) > 15 or " " in uname:[span_3](start_span)[span_3](end_span)
    print ("username tdk valid")[span_4](start_span)[span_4](end_span)
else:[span_5](start_span)[span_5](end_span)
    print ("username valid")[span_6](start_span)[span_6](end_span)
