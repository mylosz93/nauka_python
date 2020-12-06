koszyk_zakupow = [{'nazwa': 'koszula','cena':50},{'nazwa': 'spodnie','cena':100},
{'nazwa': 'majtki','cena':20},{'nazwa': 'kurtka','cena':250},{'nazwa': 'szelki',
'cena':90}]

suma = 0
for rzecz in koszyk_zakupow:
    print('{0}: {1}'.format(rzecz['nazwa'], rzecz['cena']))
    suma = suma + rzecz['cena']
print ("Suma: " + str(suma))

print ("Masz " + str(len(koszyk_zakupow)) + " rzeczy w koszyku!")

znizka = 0
if len(koszyk_zakupow) > 3 and suma < 500:
    znizka_3produkty = 0.05
    print("Twoja cena spadła o 5% bo masz więcej niż 3 pozycje w koszyku!")
    suma_znizka = suma - (suma*znizka)
    print("Suma po rabacie wynosi: " + str(suma_znizka))
if suma > 500:
    znizka_500zl = 0.1
    print("Twoja cena spadła o 10% bo masz więcej koszyk wart powyżej 500zł!")
    suma_znizka = suma - (suma*znizka_500zl)
    print ("Suma po rabacie wynosi: " + str(suma_znizka))
def najtanszy(x):
    return x['cena']
koszyk_zakupow.sort(key=najtanszy)
suma_znizka = suma_znizka - koszyk_zakupow[0]['cena']
print ('Suma po odjęciu najtańszego produktu wynosi: ' + str(suma_znizka))
