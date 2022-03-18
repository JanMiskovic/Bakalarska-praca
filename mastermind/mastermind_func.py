# Mastermind (vo funkcionálnom štýle)

# Jednoduchá hra bežiaca v termináli.
# Cieľom hry je uhádnuť náhodný 4-číselný kód.
# Na uhádnutie kódu má hráč 10 pokusov.
# Po každom pokuse získa informácie, ktoré mu pomôžu logicky prísť na správny kód.

import random
from os import system
from termcolor import colored
from tail_recursive import tail_recursive


def vycisti_terminal():
    system("cls||clear")


# Vytlačí ľubovoľné množstvo stringov s odsadením na ľavej strane.
def padded_print(*strings, sep="\n    ", end='\n'):
    print("    ", end='')
    print(*strings, sep=sep, end=end)


def vygeneruj_kod():
    return ''.join(str(random.randint(0, 9)) for _ in range(4))


def hrat_znovu():
    vstup = input("    Prajete si hrať znovu? ("
               + f"{colored('áno', on_color='on_green')} / "
               + f"{colored('nie', on_color='on_red')}): ")
    return vstup.lower() in ('ano', 'áno', 'a')


@tail_recursive
def ziskaj_vstup():
    vstup = input("    ")

    # Ak vstup nie je v správnom formáte, zavoláme funkciu znovu.
    if len(vstup) != 4 or not vstup.isnumeric():
        # Ak je vstup nesprávny, vrátime sa na začiatok riadku,
        # a vymažeme symboly po koniec riadku.
        print('\x1b[F\x1b[K', end='')
        return ziskaj_vstup.tail_call()
    else:
        return vstup


def zafarbi_vstup(vstup, kod):
    # Označíme si čísla na správnych pozíciach.
    spravne = tuple('S' if i == j else 'Z' for i, j in zip(vstup, kod))
    kod_bez_s = ''.join(' ' if i == j else j for i, j in zip(vstup, kod))
    # Označíme si čísla na ostatných pozíciach, ak sú v kóde.
    zafarbeny = zafarbi_pozicie(vstup, kod_bez_s, spravne)

    farby = {'Z': None, 'P': "on_yellow", 'S': "on_green"}
    return ''.join(colored(i, "white", farby[j]) for i, j in zip(vstup, zafarbeny))

    
@tail_recursive
def zafarbi_pozicie(vstup, kod, vystup, ix=0):
    if ix == len(kod):
       return vystup
   
    elif vstup[ix] in kod and vystup[ix] != 'S':
        novy_vystup = tuple('P' if i == ix else vystup[i] for i in range(len(vstup)))
        return zafarbi_pozicie.tail_call(vstup, kod.replace(vstup[ix], ' '), novy_vystup, ix + 1)
    else:
        return zafarbi_pozicie.tail_call(vstup, kod, vystup, ix + 1)
 

@tail_recursive()
def zacni_hru():
    vycisti_terminal()
    padded_print('', colored("MASTERMIND\n", "green"),
                    "Pravidlá hry:\n",
                    "Cieľom hry je uhádnuť náhodný 4-číselný kód.",
                    "Na uhádnutie kódu máte 10 pokusov.",
                    "Ak sa číslica v kóde nenachádza, jej farba zostane nezmenená.",
                    "Ak sa číslica v kóde nachádza, no na inej pozícii, zafarbí sa na žlto.",
                    "Ak sa číslica v kóde nachádza, a je na správnej pozícii, zafarbí sa na zeleno.\n\n")

    # Spusti hernú slučku.
    # Ak vráti True, začni ďalšiu hru, inak ukonči program.
    if herna_slucka(vygeneruj_kod(), 1):
        return zacni_hru.tail_call()
    else:
        return None


@tail_recursive
def herna_slucka(kod, pokus):
    print('\x1b[F' * pokus # Vrátime sa o n riadkov hore a prepíšeme aktuálny počet pokusov.
        + f"    Zadajte 4-číselný kód: (pokus {pokus})\n"
        + '\x1b[B' * (pokus - 1)) # Vrátime sa dole.

    vstup = ziskaj_vstup()
    zafarbeny = zafarbi_vstup(vstup, kod)
    # Vrátime sa na začiatok riadku a prepíšeme používateľov vstup zafarbeným vstupom.
    print(f"\x1b[F    {zafarbeny}", end='')

    if vstup == kod:
        padded_print('\n', colored("Uhádli ste!", "white", "on_green"),
                     f"Tajný kód bol {colored(kod, 'white', 'on_green')}.", end='\n')
        return hrat_znovu()
    
    elif pokus == 10:
        padded_print('\n', colored("GAME OVER! Neuhádli ste po 10. pokuse.", "white", "on_red"),
                         f"Tajný kód bol {colored(kod, 'white', 'on_green')}.", end='\n')
        return hrat_znovu()
    else:
        return herna_slucka.tail_call(kod, pokus + 1)


if __name__ == "__main__":
    zacni_hru()
