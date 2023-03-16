def fakt (sayi):
    if sayi == 1:
        return 1
    else:
        return sayi * fakt(sayi-1)

print(fakt(20))