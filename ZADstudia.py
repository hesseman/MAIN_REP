# ZAD. 1
# Napisz program, który sprawdza, czy z wylosowanych 3 długości boku (całkowite od 1 do 100 cm) można zbudować trójkąt i  wyświetla odpowiednią informację. 

x = int(input('Podaj pierwszą długość boku w zakresie [1, 100 cm]: '))
y = int(input('Podaj drugą długość boku [1, 100 cm]: '))
z = int(input('Podaj trzecią długośc boku [1, 100 cm]: '))
if x+y>z and y+z>x and x+z>y:
    print('Można zbudować trójkąt.')
elif x+y<z or y+z<x or x+z<y:
    print('Nie można zbudowac trójkąta.')

# ZAD. 2
# Napisz program, do którego wprowadza się promień koła w metrach. Program modyfikuje ten promień tak, aby obliczona powierzchnia koła była liczbą całkowitą. Program wyprowadza początkowe i zmodyfikowane wartości promienia i  obliczonej powierzchni. 

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

# ZAD. 5
# Napisz program, który prosi użytkownika o podanie liczby całkowitej większej od 0 (n), następnie wypisuje na ekranie sumę liczb od 1 do n. 

n = int(input('Podaj liczbę całkowitą większą od 0: '))
suma = 0
if n > 0:
    for i in range (1, n+1):
        suma = suma + i
    print(suma)
else:
    print('Zła liczba została podana.')

# ZAD. 6
# Napisz program, który wczyta od użytkownika wielkość kąta w stopniach (w zakresie od 0 do 90) i wyświetli wartość sinusa, cosinusa i tangensa o ile dla danego kąta jest to możliwe. 

from math import *
k = float(input('Podaj wielkość kąta w stopniach w zakresie (0, 90): '))
k_rd = radians(k)
if k>90 or k<0 :
    print('NIE MOŻLIWE')
elif k==90 :
    print('sin = ', sin(k_rd))
    print('cos = ', cos(k_rd))
elif k!=90 :
    print('sin = ', sin(k_rd))
    print('cos = ', cos(k_rd))
    print('tan = ', tan(k_rd))

# ZAD. 7
# Napisz program, który wykonuje losowanie liczby od 1 do 10. Następnie użytkownik wprowadza liczbę, próbując odgadnąć czy jest taka sama jak ta wylosowana. Program sprawdza czy liczby są sobie równe i wyświetla odpowiedni komunikat w przypadku sukcesu lub porażki. 

from random import *
x = randint(1, 10)
z = int(input('Spróbuj odgadnąć wylosowaną liczbę: '))
if x==z:
    print('SUKCES')
else:
    print('PORAŻKA')

# ZAD. 8
# Napisz program, który prosi użytkownika o podanie liczby całkowitej (a), a następnie wypisuje na ekranie przypadkową liczbę z zakresu od zera do podanej liczby (a). 

from random import *
a = int(input('Podaj liczbę całkowitą: '))
x = randint(0,a)
print(x)

# ZAD. 9
# Napisz program, który prosi użytkownika o podanie liczby rzeczywistej, następnie sprawdza czy jest podzielna przez 2. W zależności od parzystości wprowadzonej liczby na ekranie pojawi się odpowiednia informacja. 

x = float(input('Podaj liczbę rzeczywistą: '))
if x%2==0:
    print('Liczba jest parzysta.')
else:
    print('Liczba nie jest parzysta.')

# ZAD. 11
# Wysokość fali ekstremalnej to dwukrotność wysokości fali znacznej. Napisz program, który prosi użytkownika o podanie liczby całkowitej mniejszej od 10 (n) a następnie wypisuje na ekranie kolejne wartości fali znacznej i ekstremalnej z zakresu od 1 do n. 

x = int(input('Podaj liczbę całkowitą mniejszą od 10: '))

if x<10:
    for i in range (1, x+1):
        x = 2*x
        print('Wysokość fali ekstremalnej: ', x)
elif x>10: 
    print('Podałeś złą liczbę.')
    
if x<10:
    for i in range (1, x+1):
        x = x +1
        print('Wysokość fali znacznej: ', x)
elif x>10: 
        print('Podałeś złą liczbę.')

# ZAD. 12
# Napisz program, do którego wprowadza się promień sfery w metrach. Program modyfikuje ten promień tak, aby obliczona objętość kuli była liczbą całkowitą. Program wyprowadza obliczoną objętość kuli. 

from math import *
r = float(input('Wprowadź promień sfery w metrach: '))
R = int(r)
# print(R)
o = 4/3 * pi * R**3
O = int(o)
print('Objętość kuli wynosi: ', O)

# ZAD. 13
# Napisz program, który pyta użytkownika o temperaturę w stopniach Celsjusza, a następnie podaje tę wartość w stopniach Fahrenheita. Wzór na przeliczanie temperatury: c/5 = f-32/9 [gdzie c to temperatura w stopniach Celsjusza, f - Fahrenheita]

c = float(input('Podaj temperaturę w stopniach Celsjusza: '))
# f = c*1.8 + 32
# 5*(f - 32) = 9*c
# 5*f - 160 = 9*c
# 5*f = 9*c + 160
f = (9*c + 160)/5
print('Temperatura w stopniach Fahrenheita: ', f)

# ZAD. 14
# Napisz program, który wypisuje na ekranie liczby od 1 do 50, przy czym gdy liczba jest podzielna przez trzy, zamiast liczby wyskakuje napis "podzielna przez trzy", jeśli jest podzielna przez 5, zamiast liczby drukowane jest "podzielna przez pięć". 
# Uwaga: resztę z dzielenia sprawdzamy w następujący sposób x%3==0 (jeśli tak, to x dzieli się bez reszty przez 3).
# Przykładowy wydruk:x dz
# 1
# 2
# podzielna przez trzy
# 4
# podzielna przez pięć
# 6
# 7
# 8
# podzielna przez trzy
# podzielna przez pięć
# ........... 

from math import *
for i in range (1, 50+1):
    if i%3==0:
        print('podzielna przez trzy')
    elif i%5==0:
        print('podzielna przez pięć')
    elif i%3!=0 and i%5!=0:
        print(i)

# ZAD. 15 
# Napisz program, który pyta użytkownika o podanie dowolnego ciągu znaków, następnie wypisuje na ekranie informację, ile znaków jest w tym ciągu. 

x = input('Podaj dowolny ciąg znaków: ')
y = len(x)
print('To jest liczba znaków w tym ciągu: ', y)

# ZAD. 16
# Napisz program wyświetlający na ekranie tabliczkę mnożenia od 1 do 15. 

for i in range (0,15):
    i = i + 1
    print(i*i)

# ZAD. 17
# Napisz program, który wypisuje na ekranie kolejo 50 losowych liczb z przedziału [-100,100]. Użyj pętli for. 

from random import *
for i in range (1, 50+1):
    #x= randint(-100,100)
    i = uniform(-100,100)
    print(i)

# ZAD. 18
# Napisz program, który symuluje rzut dwudziestoma kostkami do gry i wypisuje uzyskany wynik na ekranie. 

from random import *
for i in range (1, 20+1):
    i = randint (1,6)
    print(i)

# ZAD. 19
# Napisz program proszący o nazwę użytkownika i hasło. O hasło powinien pytać dwukrotnie. Jeśli dwa razy wpisano różne hasło powinien o tym poinformować. Jeśli hasło zostało wprowadzone prawidłowo, także powinien wyświetlić odpowiedni komunikat. 

x = input('Podaj nazwę użytkownika: ')
y1 = input('Podaj hasło: ')
y2 = input('Powtórz hasło: ')
if y1 == y2:
    print('Podano dwa razy to samo hasło.')
elif y1!=y2:
    print('Hasła się nie zgadzają.')

# ZAD. 20
# Napisz program, który liczy wartość funkcji silnia dla liczb od 1 do 10. Wynik wypisuje na ekranie.
# Przykład wydruku:
# 1!=1
# 2!=2
# 3!=6
# 4!=24
# ..... 

for i in range(1,11):
    wynik=1
    for j in range (1,i+1):
        wynik=wynik*j
    print(str(i)+"!="+str(wynik))

# ZAD. 21
# Napisz program, który wypisuje na ekranie kolejno co drugą liczbę z przedziału [0,10]. Użyj pętli while. 

y = 0
while y<11:
    print(y)
    y = y + 2

# ZAD. 22
# Napisz program, który prosi użytkownika o wprowadzenie temperatury powietrzav(T [C]) i prędkości wiatru (V [km/h]), a następnie oblicza temperaturę odczuwalną za pomocą wzoru: Twc = 13.12 +0.6215*T - 11.37*V^0.16 + 0.3965*T*V^0.16. Jeżeli wprowadzona wartość prędkości wiatru będzie mniejsza od zero, na ekranie powinna pojawić się informacja, że nie można obliczyć temperatury odczuwalnej. 

t = float(input('Podaj temperaturę powietrza: '))
v = float(input('Podaj prędkość wiatru: '))
twc = 13.12 + 0.6215 * t - 11.37 * v**0.16 + 0.3965 * t * v**0.16
if v<0:
    print('Nie można obliczyć temperatuty odczuwalnej')
else:
    print('Temperatura odczuwalna wynosi: ', twc)

# ZAD. 23
# Napisz program, w którym w zależności od wartości zmiennej n(liczba całkowita większa od 0) wypisze w rzędach odpowiednią liczbę gwiazdek. Na przykład dla n = 5 wynik powinien być następujący:
# *
# **
# ***
# ****
# ***** 

a = '*'
x = int(input('Podaj liczbę całkowitą większą od 0: '))
for i in range (1, x+1):
    print(a)
    a = a +'*'

# ZAD. 24
# Napisz program, który oblicza średnią ze 1000 losowych liczb całkowitych z przedziału [-100,100]. Użyj pętli for. 

from random import *
suma = 0
for i in range (1, 1000+1):
    i = randint(-100,100)
    suma = suma + i
print(suma/1000)

# ZAD. 25
# Napisz program, który symuluje pięć losowań LOTTO (losowanie 6 numerów z zakresu 1-49). Wynik losowania drukuje na ekranie. 

from random import *
k1 = randint (1, 49)
k2 = randint (1, 49)
k3 = randint (1, 49)
k4 = randint (1, 49)
k5 = randint (1, 49)
print('Wyniki losowania to:', k1, k2, k3, k4, k5)

# ZAD. 26
# Napisz program, w którym użytkownik podaje procentowy wynik testu, a program zwraca ocenę zgodnie z następująca klasyfikacją:
# 0-51% - ndst
# 51-61% - dst
# 61-71% - dst+
# 71-81% - db
# 81-91% - db+
# 91-100% - bdb

x = int(input('Podaj procentowy wynik testu: '))
if x<0:
    print('Podałeś złą wartość.')
elif x>=0 and x<=51:
    print('Ocena niedostateczna.')
elif x>=51 and x<=61:
    print('Ocena dostateczna.')
elif x>=61 and x<=71:
    print('Ocena dostateczna +.')
elif x>=71 and x<=81:
    print('Ocena dobra.')
elif x>=81 and x<=91:
    print('Ocena dobra +.')
elif x>=91 and x<=100:
    print('Ocena bardzo dobra. :)')

# ZAD. 27
# Napisz program, który losuje liczbę całkowitą z zakresu [0,100]. Następnie pyta użytkownika o liczbę całkowitą z zakresu [0,100] i wyświetla odpowiedni komunikat:
# "Użytkowniku, podana przez Ciebie liczba jest mniejsza od wylosowanej" 
# lub
# "Użytkowniku, podana przez Ciebie liczba jest większa od wylosowanej"
# lub
# "Użytkowniku, podana przez Ciebie liczba jest taka sama jak wylosowana. GRATULACJE!!!!!!" 

from random import *
x = randint (0,100)
y = int(input('Podaj liczbę całkowitą z zakresu (0, 100): '))
# print(x, y)
if y<x:
    print('Użytkowniku, podana przez Ciebie liczba jest mniejsza od wylosowanej.')
elif y>x:
    print('Użytkowniku, podana przez Ciebie liczba jest większa od wylosowanej.')
elif x==y:
    print('Użytkowniku, podana przez Ciebie liczba jest taka sama jak wylosowana. GRATULACJE!!!!!!')

# ZAD. 28
# Napisz program, który wypisuje na ekranie liczby od 0 do 90, przy czym przed każdą liczbą podzielną przez 6 będzie gwiazdka. Uwaga: resztę z dzielenia sprawdzamy przy użyciu operatora %, np. jeśli x%3==0, to x dzieli się bez reszty przez 3.
# Przykład wydruku:
# 0
# 1
# 2
# 3
# 4
# 5
# *6
# 7
# 8
# ...

for i in range (0, 90+1):
    if i%6==0:
        print(i,'*')
    elif i%6!=0:
        print(i)

# ZAD. 29
# Napisz program, który sprawdzi, jaki procent objętości sześcianu o boku r wypełnia sfera o promieniu r. Liczba r jest definiowana przez użytkownika (wprowadzana z klawiatury). 

# ZAD. 30
# Napisz program, który pyta użytkownika o wpisanie dowolnego zdania, a następnie sprawdza ile razy w tym zdaniu występuje litera a. 

x = input('Wpisz dowolne zdanie:')
z = 

# ZAD. 31
# Napisz program, który wypisuje kolejne potęgi liczby 2 od 2 do 1024. Przykład wydruku:
# 2
# 4
# 8
# 16
# 32
# …..
suma =2
for i in range (2, 1024+1):
    suma = suma**2
print(suma)

