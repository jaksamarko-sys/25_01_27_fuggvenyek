"""1. Feladat
Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett listaelemeket (egész számokat)
 összeadja és az összegükkel tér vissza! A program tartalmazza a függvény hívását is!"""

def osszegzo(lista):
    # for i in range()
    osszeg = 0
    for num in lista:
        osszeg = osszeg + num
    return osszeg



lista = [1, 23, 63, 0, 3, 6]
print(osszegzo(lista))