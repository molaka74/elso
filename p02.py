# 2. alkalom
# from curses.ascii import isdigit

szam = input("Kérek egy számot:")
if szam.isdigit():
    szam = int(szam)
    if szam > 0:
        print("Pozitív")
    elif szam < 0:
        print("Negatív")
    else:
        print("Nulla")
else:
    print("Nem számot adtál meg!")

