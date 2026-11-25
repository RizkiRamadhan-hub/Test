print("===================================\n")[span_67](start_span)[span_67](end_span)
print("selamat datang di pembagi tagihan\n")[span_68](start_span)[span_68](end_span)
print("===================================\t")[span_69](start_span)[span_69](end_span)

try:[span_70](start_span)[span_70](end_span)
    tagihan = int(input("brp tagihannya: "))[span_71](start_span)[span_71](end_span)
    jumlahorang = int(input("brp yg patungan: "
    ))[span_72](start_span)[span_72](end_span)
    persenlayanan = int(input(
        "brp persen layanannya: "))[span_73](start_span)[span_73](end_span)
    if jumlahorang <= 0:[span_74](start_span)[span_74](end_span)
        print ("masukan yg benar")[span_75](start_span)[span_75](end_span)
        exit()[span_76](start_span)[span_76](end_span)
except:[span_77](start_span)[span_77](end_span)
    print ("masukan yg benar")[span_78](start_span)[span_78](end_span)
    exit()[span_79](start_span)[span_79](end_span)

nominallayanan = tagihan * (persenlayanan / 100)[span_80](start_span)[span_80](end_span)
total = tagihan + nominallayanan[span_81](start_span)[span_81](end_span)
totalpatungan = total / jumlahorang[span_82](start_span)[span_82](end_span)

print (f""[span_83](start_span)"[span_83](end_span)
hasil[span_84](start_span)[span_84](end_span)
tagihan: {tagihan:,.0f}Rp[span_85](start_span)[span_85](end_span)
layanan: {persenlayanan}%[span_86](start_span)[span_86](end_span)
pembayaran per orang: {totalpatungan:,.0f}Rp[span_87](start_span)[span_87](end_span)
""")[span_88](start_span)[span_88](end_span)
