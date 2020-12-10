kosz = [{"nazwa": "koszula","cena":40, "ilosc":2},
{"nazwa": "spodnie","cena":80, "ilosc":2},
{"nazwa": "majtki","cena":15, "ilosc":5},
{"nazwa": "skarpety","cena":10, "ilosc":6},]
print (kosz)

def sum_1(kosz): #opisuje sume rzeczy w koszyku bez zniżek
    sum_full = 0
    for pozycja in kosz:
        cena = pozycja["cena"]
        ilosc = pozycja["ilosc"]
        poz_cena = cena * ilosc
        sum_full = sum_full + poz_cena
    return sum_full
def sum_R4(kosz): #co trzeci produkt od ceny podstawowej gratis
    idx = 1
    sum_co3 = 0
    for pozycja in kosz:
        idx = idx + 1
        cena = pozycja["cena"]
        ilosc = pozycja["ilosc"]
        poz_cena = cena * ilosc
        if idx % 3 != 0:
            sum_co3 = sum_co3 + poz_cena
        else:
            print (".")
    return sum_co3

def sum_R1(kosz): #Jeśli więcej niż 3 rzeczy i mniej niż 500 to cena -5%
    for pozycja in kosz:
        ilosc = pozycja["ilosc"]
    if ilosc > 3 and suma_R0 < 500:
        summ_R1 = suma_R0 - (suma_R0 * 0.05)
    else:
        summ_R1 = suma_R0
    return summ_R1

def sum_R2(kosz): #Jeśli wiecej niz 500 to cena -10%
    for pozycja in kosz:
        ilosc = pozycja["ilosc"]
    if suma_1 > 500:
        summ_R2 = suma_R0 - (suma_R0 * 0.1)
    elif suma_R1 < suma_R0:
        summ_R2 = suma_R1
    return summ_R2

def sum_R3(kosz): #od najniższej ceny odjąć cenę najtańszego produktu
    lista_cen = [suma_R0,suma_R1,suma_R2]
    min_cena = min(pozycja["cena"]for pozycja in kosz)
    summ_R3 = min(lista_cen) - min_cena
    return summ_R3

suma_1 = sum_1(kosz)
print ("Suma koszyka bez żadnych zniżek wynosi: " + str(suma_1))
suma_R0 = sum_R4(kosz)
print ("Dzisiaj co 3 produkt gratis! Twoja cena wynosi: " + str(suma_R0))
suma_R1 = sum_R1(kosz)
print ("Jeśli w koszyku jest więcej niż 3 przedmioty to cena spada o 5%. Twoja cena wynosi: " + str(suma_R1))
suma_R2 = sum_R2(kosz)
print ("Jeśli wydaleś ponad 500zł to dostaniesz 10% rabatu. Twoja cena to: " + str(suma_R2))
suma_R3 = sum_R3(kosz)
print ("gratuluję, od Twojej dzisiejszej najniższej ceny odjęto cenę najniższego produktu. Twoj cena wynosi: " + str(suma_R3))
