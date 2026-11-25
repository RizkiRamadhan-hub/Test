def hitung_nilai():[span_29](start_span)[span_29](end_span)
    while True:
        try:[span_30](start_span)[span_30](end_span)
            nilai = int(input("masukan nilai anda: "
            ))[span_31](start_span)[span_31](end_span)
        except:[span_32](start_span)[span_32](end_span)
            print ("masukan nilai yg benar")[span_33](start_span)[span_33](end_span)
            continue

        if 80 <= nilai <= 100:[span_34](start_span)[span_34](end_span)
            print ("A")[span_35](start_span)[span_35](end_span)
            break
        elif 75 <= nilai <= 84:[span_36](start_span)[span_36](end_span)
            print ("B")[span_37](start_span)[span_37](end_span)
            break
        elif 60 <= nilai <= 74:[span_38](start_span)[span_38](end_span)
            print ("C")[span_39](start_span)[span_39](end_span)
            break
        elif 0 <= nilai <= 59:[span_40](start_span)[span_40](end_span)
            print ("D")[span_41](start_span)[span_41](end_span)
            break
        else:[span_42](start_span)[span_42](end_span)
            print ("masukan yg benar, 0 - 100")[span_43](start_span)[span_43](end_span)

hitung_nilai()[span_44](start_span)[span_44](end_span)
