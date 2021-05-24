import math #import bibliotek w Pythonie; potrzebna do obliczania pierwiastka z delty


def oblicz_delte(a, b, c): #definiowanie funkcji w Pythonie; oblicza ona delte z podanych a b c
    delta = b * b - 4 * a * c #inicjalizacja zmiennych w Pythonie; zmienna pomocnicza;
    return delta #zwracanie wartości w funkcji Python; zwracamy delte


print("Program obliczajacy rozwiazania rownania kwadratowego") #drukowanie do konsoli w Pythonie
print("Rownanie ma postac: ax^2 + bx + c = 0")
print("Podaj liczbe a:")
a = float(input()) #input() to pobieranie danych od uzytkownika
print("Podaj liczbe b:")
b = float(input()) #float() ma za zadanie pobrac te dane jako liczby rzeczywiste
print("Podaj liczbe c:")
c = float(input())
if a != 0: #warunek w Pythonie; musimy sprawdzic, czy a != 0 - wtedy mamy pewnosc, ze mamy do czynienia z rownaniem kwadratowym
    delta = oblicz_delte(a, b, c) #korzystamy ze zdefiniowanej funkcji
    if delta < 0: #rozwazamy przypadki: delta < 0 - brak rozwiazan
        print("Brak rozwiazan")
    if delta == 0: #rozwazamy przypadki: delta == 0 - jedno rozwiazanie
        x0 = -b/(2*a) #obliczamy zgodnie ze wzorem
        print ("Jedno rozwiazanie. x0 = ", x0) #a nastepnie wypisujemy
    if delta > 0: #rozwazamy przypadki: delta > 0 - dwa rozwiazania
        sqrdelta = math.sqrt(delta) #obliczamy pierw. z delty, przy uzyciu importowanej biblioteki math
        x1 = (-b - sqrdelta)/(2*a) #a nastepnie obliczamy rozwiazania zgodnie ze wzorami
        x2 = (-b + sqrdelta) / (2 * a)
        print("Dwa rozwiazania. x1 = ", x1, "x2=", x2) #i je wypisujemy
else:
    print("To nie jest rownanie kwadratowe.") #gdy a==0, to nie jest wtedy rownanie kwadratowe