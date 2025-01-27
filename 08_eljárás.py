"""4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!"""

def feladat(x):
    szavak = []
    for i in range(x):
        szo = input("Írj be 1 szót: ")
        szavak.append(szo)
    print(szavak)
    print(min(szavak,key=len))






hanyszor = 4
feladat(hanyszor)