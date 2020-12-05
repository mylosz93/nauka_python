zawodnik = {'imie': 'George Paul','klub': 'Clippers',
            'wiek': '31' }
print(zawodnik['imie'])
print(zawodnik['klub'])
for key in zawodnik:
    print("{0}:{1}".format(key, zawodnik[key]))
for key,value in zawodnik.items():
    print("{0}:{1}".format(key, value))
