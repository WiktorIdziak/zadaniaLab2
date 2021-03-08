#Zad1
'''filmy=["Boro na 10","Lord of the Rings","Trailer Park Boys","Tytanic","Ojciec Chrzestny"]
print(filmy)
filmy.reverse()
print(filmy)
filmy.insert(5,"Ratchet & Clank")
filmy.insert(5,"Shrek")
filmy.insert(5,"Zielona Mila")
filmy.insert(5,"The Room")
filmy.insert(5,"Matrix")
print(filmy)'''
#Zad2
'''slownik={1:"Boro na 10", 2:"Lord of the Rings",3:"Trailer Park Boys",4:"Tytanic",5:"Ojciec Chrzestny",6:"Ratchet & Clank",7:"Shrek",8:"Zielona Mila",9:"The Room",10:"Matrix"}'''
#Zad3
'''slownik={"WZ":"Wizualizacja danych","CAD":"CAD komputerowe wspomaganie programowania","Rch R&C":"Rachunek różniczkowy i całkowy","EMD":"Elementy matematyki dyskretnej","PS":"Programowanie Strukturalne"}
print(slownik.__len__())'''
#Zad4
'''napis= input("Podaj liczbę: ")
liczba = eval(napis)
wynik= liczba*liczba
print(wynik)'''
#Zad5
'''licznikA = 0
notatnik = open("plik.txt","r").read()
linie = notatnik.split("\n")
for linia in linie:
    for znak in linia:
        if znak == 'a':
            licznikA+=1
print(licznikA)'''
#Zad6
'''a = eval(input("Podaj liczbe A: "))
b = eval(input("Podaj liczbe B: "))
c = eval(input("Podaj liczbe C: "))
print(a)
if a%2==0 and b>c:
    print("TAK")
else:
    print("NIE")'''
#Zad7
'''lista = [1,2.5,4,5.5,7,8.5,10]
i=0;
while(i<lista.__len__()-1):
    wynik = lista[i] + lista[i+1]
    print(wynik)
    i+=1'''
#Zad8
'''i=0
lista = []
while(i<10):
    liczba = eval(input("Podaj liczbe: "))
    if liczba % 1 == 0:
        lista.append(liczba)
    i+=1
print(lista)'''
#Zad9
'''lista = [1,2,3,4,5,6]
tekst=""
for y in lista:
    if y != 1 and y != 6:
       print("O    O")
    for x in lista:
        if x==1 and y==1:
            print("OOOOOO")
        elif x == 1 and y == 6:
            print("OOOOOO")
print(tekst)'''
#Zad10
'''liczba = input("Podaj liczbe: ")
try:
    liczba = int(liczba)
except ValueError:
    print("Podana wartosc nie jest wartoscia liczbowa")'''