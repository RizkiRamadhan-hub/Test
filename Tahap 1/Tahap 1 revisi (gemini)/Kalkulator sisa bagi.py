print("===================================\n")[span_8](start_span)[span_8](end_span)
print("selamat datang di kalkulator sisa bagi\n")[span_9](start_span)[span_9](end_span)
print("===================================\t")[span_10](start_span)[span_10](end_span)

print("kalkulator sisa bagi adalah program yg dibuat utk mengonversi detik ke menit"
)[span_11](start_span)[span_11](end_span)

while True:[span_12](start_span)[span_12](end_span)
    try:[span_13](start_span)[span_13](end_span)
        masukan = int(input("masukan detik: "))[span_14](start_span)[span_14](end_span)
        menit = masukan // 60[span_15](start_span)[span_15](end_span)
        detik = masukan % 60[span_16](start_span)[span_16](end_span)
        print(f"hasil: {menit:,}:{detik:02d} menit")[span_17](start_span)[span_17](end_span)
    except ValueError:[span_18](start_span)[span_18](end_span)
        print("masukan angka bulat")[span_19](start_span)[span_19](end_span)
        break[span_20](start_span)[span_20](end_span)
    except:[span_21](start_span)[span_21](end_span)
        print ("error")[span_22](start_span)[span_22](end_span)

    lagi = input(
        "apakah anda mau hitung lagi (y/n): ")[span_23](start_span)[span_23](end_span)
    if lagi.lower() == "y":[span_24](start_span)[span_24](end_span)
        pass[span_25](start_span)[span_25](end_span)
    else:[span_26](start_span)[span_26](end_span)
        print ("program selesai")[span_27](start_span)[span_27](end_span)
        break
