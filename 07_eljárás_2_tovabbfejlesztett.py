













'''Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!'''

def feladat(szam):  
    if szam > 0:
        print("A szám pozitív.")
    elif szam < 0:
        print("A szám kisebb mint nulla")
    else:    
        print("A szám nulla")


run = True

while run:
    num = (input("Adj meg egy számot: "))
    if num == "":
        run = False
        break
    num = int(num)
    feladat(num)

