# -*- coding: utf-8 -*-
d = [10, 8, 10, 12, 6, 8, 7, 12, 10, 16, 16, 9, 14, 9, 11, 17, 18, 9,
     5, 17, 11, 17, 7, 7, 12, 9, 5, 18, 6, 7, 9, 9, 6, 8, 8, 11, 13,
     16, 8, 8, 12, 5, 18, 15, 17, 18, 7, 8, 13, 5, 12, 11, 11, 12, 5,
     17, 7, 15, 10, 14, 18, 5, 8, 9, 10, 14, 15, 13, 16, 14, 17, 16, 10,
     7, 14, 15, 17, 11, 10, 18, 18, 9, 12, 18, 12, 13, 7, 10, 16, 12, 16,
     8, 11, 15, 8, 7, 7, 10, 13, 13]
c = list(d)
print(c[5:15])
print(d[:5])  # do 5 liczb w lissie
a = 'Tomasz'
b = 'Pielecki'
e = 34
print("ilosc", len(d))
print("max", max(d))
print("min", min(d))

print("-------------------")
# funkcje
def value():
    print("min", min(d)),
    print("max", max(d)),
    print("ilosc", len(d))
    return
value()


def person():
    print(a, b, e)
    return
person()

def powiedzAhoj():
    print('Ahoj, przygodo!')  # Blok należący do funkcji.
powiedzAhoj()  # Wywołanie funkcji.
powiedzAhoj()  # Ponowne wywołanie funkcji.
value()

def my_function(Name):
    print(Name + " is a student WSB"),
my_function ("Tomasz")

def my_function1(firstName, secondName):
    print(firstName + " " + secondName + " " + ' Mechanic in Grzybno')
my_function1 ("Adam ", "Popiel")
my_function1("Andrzej", "Stary")
my_function1("Michał", "Zakościelny")
my_function1("Dominik", "Wazonik")

def sum(x,y) :
    print(x+y)
sum(3,4)

def odd(x,y) :
    o = x-y
    return o
print("odd(6,4)=",odd(6,4))

def mno(x,y) :
    print(x*y)
mno(7,4)
def dziel(x,y) :
    print(int(x/y))
dziel(8,4)


#słowniki
Personer = {


}