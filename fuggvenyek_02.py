"""2. Feladat
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza, ha a paraméterként átvett 
listaelemek (egész számok) között van páros, ellenkező esetben a visszatérési érték False! A program tartalmazza a függvény hívását is!
"""

def paros_e(nums):
    for num in nums:
        if num % 2 == 0:
            print(num)
            return True

    return False


numbers = [1, 57, 3, 1, 2]
print(paros_e(numbers))