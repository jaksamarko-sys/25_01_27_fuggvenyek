'''Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!'''

def feladat(szam):  
    if szam > 0:
        print("A szám pozitív.")
    if szam < 0:
        print("A szám kisebb mint nulla")
    else:    
        print("A szám nulla")


num = int(input("Adj meg egy számot: "))
feladat(num)