def ucgen_mi(a,b,hipotenüs):
    if (a**2 + b**2 == hipotenüs**2):
        return "bu bir dik üçgendir"
    else:
        return "bu bir dik üçgen deildir"
print(ucgen_mi(3,4,5))