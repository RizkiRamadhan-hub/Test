print("===================================\n")[span_46](start_span)[span_46](end_span)
print("selamat datang di konverter suhu celcius ke fahrenheit\n"
)[span_47](start_span)[span_47](end_span)
print("===================================\t")[span_48](start_span)[span_48](end_span)

while True:[span_49](start_span)[span_49](end_span)
    try:[span_50](start_span)[span_50](end_span)
        celcius = float(input("suhu celcius: "))[span_51](start_span)[span_51](end_span)
        fahrenheit = (celcius * 9/5) + 32[span_52](start_span)[span_52](end_span)
        print (f"hasil: {fahrenheit:.2f} fahrenheit")[span_53](start_span)[span_53](end_span)

        if celcius > 35:[span_54](start_span)[span_54](end_span)
            print ("suhu panas")[span_55](start_span)[span_55](end_span)
        elif 20 <= celcius <= 35:[span_56](start_span)[span_56](end_span)
            print ("suhu normal")[span_57](start_span)[span_57](end_span)
        else:[span_58](start_span)[span_58](end_span)
            print ("sejuk")[span_59](start_span)[span_59](end_span)
    except ValueError:[span_60](start_span)[span_60](end_span)
        print("masukan angka desimal")[span_61](start_span)[span_61](end_span)
        continue[span_62](start_span)[span_62](end_span)
    except:[span_63](start_span)[span_63](end_span)
        print ("error")[span_64](start_span)[span_64](end_span)

    lagi = input(
        "apakah anda mau hitung lagi (y/n): ")[span_65](start_span)[span_65](end_span)
    if lagi.lower() == "y":
        pass
    else:
        print("program selesai")
        break
