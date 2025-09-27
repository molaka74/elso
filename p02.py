# 2. alkalom
# from curses.ascii import isdigit

'''szam = input("Kérek egy számot:")
if szam.isdigit():
    szam = int(szam)
    if szam > 0:
        print("Pozitív")
    elif szam < 0:
        print("Negatív")
    else:
        print("Nulla")
else:
    print("Nem számot adtál meg!")'''
from random import random

'''
jegy = int(input("Kérek egy érdemjegyet:"))
while jegy == 1 or jegy > 5 or jegy < 1:
    jegy = int(input("Kérek egy érdemjegyet:"))
    if jegy == 10:
        print("Csillagos ötös!")
        break
else:
    print("Jól teljesített")
print("Gratulálunk") '''
'''
kocka = random.randint(1, 6)
while True:
    tipp = int(input("Kérek egy tippet: "))
    if tipp == kocka:
        break
print("Sikerült eltalálnod a számot!")'''
'''
uzenet = "Jó reggelt!"
for betu in uzenet:
    print(betu)
    if betu == "":
        break'''
'''
def fv():
    pass

for elem in range(1, 6):
    if elem == 3:
        continue
    print(elem, "Nem leszek többet rossz!")'''
'''
try:
    print(10/5)
except ZeroDivisionError:
    print("Hiba! Nullával osztás!")
except NameError:
    print("Hiba! Név hiba")
print("Ok")'''

while True:
    try:
        szam = int(input("Kérek egy egész számot:"))
    except:
        print("Nem egész számot adott meg!")
    else:
        break
