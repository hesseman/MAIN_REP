# ZAD. 1
# Napisz program, który sprawdza, czy z wylosowanych 3 długości boku (całkowite od 1 do 100 cm) można zbudować trójkąt i wyświetla odpowiednią informację. 

x = int(input('Podaj pierwszą długość boku w zakresie [1, 100 cm]: '))
y = int(input('Podaj drugą długość boku [1, 100 cm]: '))
z = int(input('Podaj trzecią długośc boku [1, 100 cm]: '))
if x+y>z and y+z>x and x+z>y:
    print('Można zbudować trójkąt.')
elif x+y<z or y+z<x or x+z<y:
    print('Nie można zbudowac trójkąta.')

# ZAD. 2
# Napisz program, do którego wprowadza się promień koła w metrach. Program modyfikuje ten promień tak, aby obliczona powierzchnia koła była liczbą całkowitą. Program wyprowadza początkowe i zmodyfikowane wartości promienia i obliczonej powierzchni. 

from math import * 
r = float(input('Wprowadź promień koła: '))
R = int(r)
print('Początkowa wartość promienia: ', r)
print('Zmodyfikowana wartość promienia: ', R)
P = pi * R**2
print('Powierzchnia koła wynosi: ', P)

# ZAD. 3
# Napisz program, który losuje 3 całkowite współczynniki równania kwadratowego z przedziału [-10,10]. Następnie oblicza pierwiastki tego równania. Na koniec wypisuje na ekranie wylosowane współczynniki i pierwiastki równania (rozwiązanie równania kwadratowego). 

from random import *
import math 
a = randint(-10, 10)
b = randint(-10, 10)
c = randint(-10, 10)
delta = b**2 - 4* a * c
p1 = -b - math.sqrt(delta)/2*a
p2 = -b + math.sqrt(delta)/2*a
p3 = -b/2*a
if delta !=0:
    print('Pierwiatki równania wynoszą: ',p1, 'i', p2)
elif delta == 0:
    print('Pierwiastek równania wynosi: ', p3)
elif delta<0:
    print('To równanie nie ma pierwiastków.')
    
# ZAD. 4
# Napisz program, który wykonuje 1000 losowań trzema kostkami do gry i wypisuje na ekranie ile razy w trakcie tych 1000 rzutów wypadły równocześnie trzy szóstki. 

from random import *
k1 = randint(1,6)
k2 = randint(1,6)
k3 = randint(1,6)
suma = 0
for i in range (1001):
    k1 = randint(1,6)
    k2 = randint(1,6)
    k3 = randint(1,6)
    if k1==6 and k2==6 and k3==6:
        print('Sukces')
        suma = suma +1
print(suma)
    
