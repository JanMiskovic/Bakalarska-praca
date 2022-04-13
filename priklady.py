# Nemenné dátové štruktúry
# Jednoduchý príklad

# Imperatívna paradigma
plat = 1000
plat += 300
plat = plat * 0.75
# print(plat) # 975

# Funkcionálna paradigma
hruba_mzda = 1000
navysena_mzda = hruba_mzda + 300
cista_mzda = navysena_mzda * 0.75
# print(cista_mzda) # 975


# Príklad s kolekciami

# Imperatívna paradigma
mena = ["marek", "viktor", "michal"]
for i in range(len(mena)):
    mena[i] = mena[i].capitalize()
# print(mena) # ["Marek", "Viktor", "Michal"]

# Funkcionálna paradigma
mena = ("marek", "viktor", "michal")
kap_mena = tuple(i.capitalize() for i in mena)
# print(kap_mena) # ("Marek", "Viktor", "Michal")


# Príklad s modulom pyrsistent

# Modul pyrsistent
from pyrsistent import pvector

mesta = pvector(["Košice", "Nitra", "Trnava"])
s_bratislavou = mesta.append("Bratislava")
nahradeny_stred = mesta.set(1, "Žilina")
bez_nitry = mesta.remove("Nitra")
bez_prveho = mesta.delete(0)

# print(mesta, s_bratislavou, nahradeny_stred, bez_nitry, bez_prveho, sep="\n")


# Pravé funkcie
# Príklad rôznych nepravých funkcií

hodnota = 10

# Mutácia globálnej premennej
def prva():
    global hodnota
    hodnota += 5

# Mutácia lokálnej premennej
def druha():
    zoznam = []
    zoznam.append(5)
    return zoznam

# Mutácia argumentu
def tretia(zoznam):
    zoznam[0] = 0
    return zoznam

# Prístup k nelokálnej premennej
def stvrta():
    nova = hodnota + 5
    return nova

# print(prva(), druha(), tretia([1, 2]), stvrta())


# Príklad zmeny stavu programu

# Imperatívna paradigma
hodnota = 10

def zvys_hodnotu():
    zvysenie = int(input())
    global hodnota
    hodnota += zvysenie
    
# zvys_hodnotu()
# print(hodnota)

# Funkcionálna paradigma
def vytvor_hodnotu():
    return 10

def zvys_hodnotu(hodnota, zvysenie):
    return hodnota + zvysenie

# print(zvys_hodnotu(vytvor_hodnotu(),
                   # int(input())))


# Rekurzia
# Fibonacciho čísla

# Imperatívna paradigma
def ifib(n):
    fib, a, b = 0, 0, 1
    
    for i in range(n):
        a = fib + b
        fib = b
        b = a
        
    return fib

# print(ifib(10)) # 55

# Funkcionálna paradigma
def ffib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return ffib(n-1) + ffib(n-2)
    
# print(ffib(100)) # 55


# Faktoriál v pravej a chvostovej rekurzii 

# Rekurzia
def fac(n):
    if n == 0: return 1
    else: return n * fac(n-1)
    
# print(fac(5)) # 120

# Chvostová rekurzia
def chfac(n, f=1):
    if n == 1: return f
    else: return chfac(n-1, f*n)
    
# print(chfac(5)) # 120


# Knižnica tail-recursive

# Bez optimalizácie
def fac(n, f=1):
    if n == 1: return f
    else: return fac(n-1, f*n)
    
# print(fac(1000)) # RecursionError

# Modul tail-recursive
from tail_recursive import tail_recursive

@tail_recursive
def ofac(n, f=1):
    if n == 1: return f
    else: return ofac.tail_call(n-1, f*n)
    
# print(ofac(1000)) # 4023872600770...


# Funkcie vyššieho rádu
# Anonymné funkcie - Príklad anonymnej funkcie

# Bežná funkcia
def odmocnina(a, b):
    return a ** (1 / b)
    
# Anonymná funkcia 
lambda a, b: a ** (1 / b)

# print(odmocnina(64, 2))
# print((lambda a, b: a ** (1 / b))(64, 2))


# Anonymné funkcie - Príklad s trojčlenným operátorom

# Trojčlenný operátor
lambda x: "nepárne" if x % 2 else "párne"


# Anonymné funkcie - Príklad nepravej a pravej anonymnej funkcie

povolene_cisla = (1, 3, 4, 5, 9)

# Nepravá anonymná funkcia
lambda x: "povolené" if x in povolene_cisla else "zakázane"

# Pravá anonymná funkcia
lambda x, p=povolene_cisla: "povolené" if x in p else "zakázane"


# Map - Príklad s jednou kolekciou a anonymnou funkciou

# Imperatívna paradigma
cisla = [1, 2, 3]
cisla2x = []
for i in cisla:
    cisla2x.append(i * 2)

# print(cisla2x) # [2, 4, 6]

# Funkcionálna paradigma
cisla = (1, 2, 3)
cisla2x = map(lambda x: x * 2, cisla)

# print(tuple(cisla2x)) # (2, 4, 6)


# Map - Príklad s viacero kolekciami

# Viacero kolekcií
cisla = (1, 2, 3, 4)
expon = (5, 4, 3, 2, 1)
umocnene = map(pow, cisla, expon)

# print(tuple(umocnene)) # (1, 16, 27, 16)


# Filter - Príklad s anonymnou funkciou

# Imperatívna paradigma
cisla = range(10, 20)
parne = []
for i in cisla:
    if i % 2 == 0:
        parne.append(i)
        
# print(parne)
# [10, 12, 14, 16, 18]


# Funkcionálna paradigma
cisla = range(10, 20)
parne = filter(lambda x: x % 2 == 0, cisla)

# print(tuple(parne))
# (10, 12, 14, 16, 18)


# Filter - Negácia bežnej funkcie a filterfalse

prvky = ("1", "2", "3", "a", "b", "c", " ")

# Obalenie anonymnou funkciou
bez_cisel = filter(lambda x: not str.isnumeric(x), prvky)
# print(tuple(bez_cisel)) # ("a", "b", "c", " ")

# Filterfalse
from itertools import filterfalse

bez_cisel = filterfalse(str.isnumeric, prvky)
# print(tuple(bez_cisel)) # ("a", "b", "c", " ")


# Filter - None namiesto funkcie

prvky = (-1, 0, 1, "", "a", [], False, True, None)

# Použitie None namiesto funkcie
true_prvky = filter(None, prvky)
# print(tuple(true_prvky)) # (-1, 1, "a", True)

false_prvky = filterfalse(None, prvky)
# print(tuple(false_prvky)) # (0, "", [], False, None)


# Reduce - Príklad s anonymnou funkciou


# Imperatívna paradigma
cisla = range(1, 6)
sucin = 1
for i in cisla:
    sucin *= i

# print(sucin) # 120

# Funkcionálna paradigma
from functools import reduce

cisla = range(1, 6)
sucin = reduce(lambda ak, x: ak * x, cisla)

# print(sucin) # 120


# Reduce - Príklad s modulom operator

# Modul operator
from operator import mul

cisla = range(1, 6)
sucin = reduce(mul, cisla)

# print(sucin) # 120


# Užitočné funkcie na kolekcie - Príklad funkcie all a any

cisla = (1, 2, 5, 8, 10)

# All v kombinácii s map
vsetky_parne = all(map(lambda x: x % 2 == 0, cisla))
# print(vsetky_parne) # False

# Any v kombinácii s map
aspon_jedno_neparne = any(map(lambda x: x % 2 == 1, cisla))
# print(aspon_jedno_neparne) # True


# Užitočné funkcie na kolekcie - Príklad funkcie max a min

retazce = ("prvý", "druhý", "desiaty")

# Max s vyplneným parametrom key
najdlhsi = max(retazce, key=len)
# print(najdlhsi) # "desiaty" 

# Min s vyplneným parametrom key
najkratsi = min(retazce, key=len)
# print(najkratsi) # "prvý"


# Užitočné funkcie na kolekcie - Príklad funkcie sum

cisla = (1, 2, 3, 5, 8)

# Sum v kombinácii s map
pocet_parnych = sum(map(lambda x: x % 2 == 0, cisla))
# print(pocet_parnych) # 2


# Užitočné funkcie na kolekcie - Príklad funkcie sorted

retazce = ("raz", "dva", "tri", "štyri")

# Sorted s vyplneným parametrom key
podla_posledneho = sorted(retazce, key=lambda x: x[-1])
# print(podla_posledneho) # ["dva", "tri", "štyri", "raz"]


# Funkcie vracajúce funkcie - Funkcia časovač

from time import perf_counter

# Funkcia časovač
def casovac(funkcia):
    def obal(*args, **kwargs):
        start = perf_counter()
        vysledok = funkcia(*args, **kwargs)
        koniec = perf_counter()
        print(round(koniec - start, 8), "sekúnd")
        return vysledok
    return obal

def velke_umocnenie(n):
    return n ** (10 ** 6)

umocnenie_s_casovacom = casovac(velke_umocnenie)

# umocnenie_s_casovacom(5) # 0.1275 sekúnd
# umocnenie_s_casovacom(50) # 0.4952 sekúnd


# Dekorátory - Použitie dekorátora

# Bez dekorátora
def umocnenie(n):
    return n ** (10 ** 6)

umocnenie = casovac(umocnenie)

# vysledok = umocnenie(5)
# 0.1249 sekúnd

# Dekorátor
@casovac
def umocnenie(n):
    return n ** (10 ** 6)

# vysledok = umocnenie(5)
# 0.1249 sekúnd


# Dekorátory - Dekorátor cache

# Dekorátor cache
from functools import cache

@cache
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1) + fib(n-2)

@casovac    
def obal_fib(n):
    fib(n)
    
obal_fib(20) # Bez cache - 0.02s; Cache - 0.000058s  
obal_fib(30) # Bez cache - 2.62s; Cache - 0.000027s 
obal_fib(35) # Bez cache - 29.1s; Cache - 0.000010s


# Generátorová notácia - Porovnanie s for cyklom

# For cyklus
zoznam = []
for i in range(5):
    zoznam.append(i * 2)
    
# print(zoznam)
# [0, 2, 4, 6, 8]

# Generátorová notácia
zoznam = [i * 2 for i in range(5)]

# print(zoznam)
# [0, 2, 4, 6, 8]


# Generátorová notácia - Príklad vnorených for

# Vnorený zoznam na rovnú n-ticu
vnoreny = [(1, 2), (3, 4), (5, 6), (7, 8)]

rovny = tuple(prvok for ntica in vnoreny for prvok in ntica)
# print(rovny) # (1, 2, 3, 4, 5, 6, 7, 8)


# Generátorová notácia - Príklad vnorenej notácie

# Vytvorenie 4x2 matice naplnenej nulami
matica = [[0 for _ in range(4)] for _ in range(2)]

# print(matica) # [[0, 0, 0, 0], [0, 0, 0, 0]]


# Generátorová notácia - Príklad s funkciou zip

# Príklad s funkciou zip
cisla = (1, 2, 3, 4, 5)
expon = (5, 4, 3, 2, 1)

umocnene = (pow(c, e) for c, e in zip(cisla, expon))
# print(tuple(umocnene)) # (1, 16, 27, 16, 5)


# Generátorová notácia - Príklad s funkciou enumerate a podmienkou

# Príklad s funkciou enumerate a podmienkou
mesta = ["Nitra", "Trnava", "Hlohovec", "Galanta"]

neparne_indexy = [p for indx, p in enumerate(mesta) if indx % 2]
# print(neparne_indexy) # ["Trnava", "Galanta"]


# Generátorová notácia - Nahradenie map a filter

mesta = ["Nitra", "Trnava", "Hlohovec", "Galanta"]

# Map a filter
konciace_na_a = filter(lambda x: x[-1] == "a", mesta)
prevratene = map(lambda x: x[::-1], konciace_na_a)

# print(list(prevratene))
# ['artiN', 'avanrT', 'atnalaG']

# Generátorová notácia
vysledok = [i[::-1] for i in mesta if i[-1] == "a"]

# print(vysledok)
# ['artiN', 'avanrT', 'atnalaG']