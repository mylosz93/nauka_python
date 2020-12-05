lista_pilkarzy = ['Putnocky','Pawelec','Celeban','Stiglec','Puerto','Sobota']
print(len(lista_pilkarzy))
print(lista_pilkarzy[-1])
print('........')

for i in lista_pilkarzy:
    print(i)
for nr in range(len(lista_pilkarzy)):
    print("nr: " + str(nr) + " : " + lista_pilkarzy[nr])
print('.'*15)
print("")
while True:
    dodaj = input("podaj nazwisko piłkarza którego chcesz dodać do listy: (Jeśli nie chcesz dodawać więcej piłkarzy wpisz 'n')")
    lista_pilkarzy.append(dodaj)
    if dodaj == 'n':
            break
    print(lista_pilkarzy)
