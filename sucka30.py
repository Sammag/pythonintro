saldo=5000

print("Det fantastiska bankdank")
print("========================")
print("val 1: insattning")
print("val 2: uttdrag")
print("val 3: saldo")
print("val 4; avsluta")

val = int(input("välj ditt val"))

if val == 1:
    insattning=int(input("hur mycket vill du sätta in"))
    valuta= valuta  - insattning
    print("din valuta :", valuta)

elif val ==2: 
        uttdrag =int(input("hur mycket vill du ta ut"))
        valuta= valuta - uttdrag
        print("din valuta:", valuta)
elif val ==3:
        saldo= int(input("saldo "))
elif val ==4:
    print("tack för att du använde bankdank")


