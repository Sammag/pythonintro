valuta=50000

print("Det fantastiska bankdank")
print("========================")
print("val 1: insättning")
print("val 2: uttdrag")
print("val 3: visa saldo")
print("val 3; avsluta")

val = int(input("välj ditt val")


if val == 1: 
insättning =int(input("hur mycket vill du sätta in"))
valuta= valuta  - insättning
print("din valuta :", valuta)

elif val ==2: 
        uttdrag =int(input("hur mycket vill du ta ut"))
        valuta= valuta - uttdrag
        print("din valuta:", valuta)
elif val ==3:
        saldo= int(input("din saldo "))
elif val ==4:
input("tack för att du använde bankdank")


