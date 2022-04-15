# Mastermind (v procedurálnom štýle).

# Jednoduchá hra bežiaca v termináli.
# Cieľom hry je uhádnuť náhodný 4-číselný kód.
# Na uhádnutie kódu má hráč 10 pokusov.
# Po každom pokuse získa informácie, ktoré mu pomôžu logicky prísť na správny kód.

import random
from os import system
from termcolor import colored

pokus = 0
kod = []
hrat = True


def vycisti_terminal():
    system("cls||clear")


# Vytlačí ľubovoľné množstvo stringov s odsadením na ľavej strane.
def padded_print(*strings, sep="\n    ", end='\n'):
    print("    ", end='')
    print(*strings, sep=sep, end=end)


def vygeneruj_kod():
    global kod
    kod = []
    for _ in range(4):
        kod.append(str(random.randint(0, 9)))


def hrat_znovu():
    global hrat
    vstup = input("    Prajete si hrať znovu? ("
               + f"{colored('áno', 'white', 'on_green')} / "
               + f"{colored('nie', 'white', 'on_red')}): ")
    hrat = vstup.lower() in ('ano', 'áno', 'a')


def ziskaj_vstup():
    vstup = input("    ")

    while(len(vstup) != 4 or not vstup.isnumeric()):
        # Ak je vstup nesprávny, vrátime sa na začiatok riadku,
        # a vymažeme symboly po koniec riadku.
        print('\x1b[F\x1b[K', end='')
        vstup = input("    ")

    return [i for i in vstup]


def zafarbi_vstup(vstup):
    zafarbeny = ['Z', 'Z', 'Z', 'Z']
    t_kod = kod.copy()

    # Označíme si čísla na správnych pozíciach.
    for ix, (i, j) in enumerate(zip(vstup, t_kod)):
        if i == j:
            zafarbeny[ix] = 'S' # Správne
            t_kod[ix] = ' '

    # Označíme si čísla na ostatných pozíciach, ak sú v kóde.       
    for ix, (i, j) in enumerate(zip(vstup, t_kod)):
        if i in t_kod and zafarbeny[ix] == 'Z':
            zafarbeny[ix] = 'P' # Pozícia
            t_kod[t_kod.index(i)] = ' '

    pozadia = {'Z': None, 'P': "on_yellow", 'S': "on_green"}
    farby = {'Z': None, 'P': "white", 'S': "white"}
    return ''.join(colored(i, farby[j], pozadia[j]) for i, j in zip(vstup, zafarbeny))


def zacni_hru():
    while(hrat):
        vycisti_terminal()
        padded_print('', colored("MASTERMIND\n", "green"),
                     "Pravidlá hry:\n",
                     "Cieľom hry je uhádnuť náhodný 4-číselný kód.",
                     "Na uhádnutie kódu máte 10 pokusov.\n",
                     "Ak sa číslica v kóde nenachádza, jej farba zostane nezmenená.",
                     "Ak sa číslica v kóde nachádza, no na inej pozícii, zafarbí sa na žlto.",
                     "Ak sa číslica v kóde nachádza, a je na správnej pozícii, zafarbí sa na zeleno.\n\n")

        global pokus
        pokus = 1
        vygeneruj_kod()

        while pokus <= 10:
            print('\x1b[F' * pokus # Vrátime sa o n riadkov hore a prepíšeme aktuálny počet pokusov.
                + f"    Zadajte 4-číselný kód: (pokus {pokus})\n"
                + '\x1b[B' * (pokus - 1)) # Vrátime sa dole.

            vstup = ziskaj_vstup()
            zafarbeny = zafarbi_vstup(vstup)
            # Vrátime sa na začiatok riadku a prepíšeme používateľov vstup zafarbeným vstupom.
            print(f"\x1b[F    {zafarbeny}", end='')

            # Skontrolujeme výhru.
            if vstup == kod:
                padded_print('\n', colored("Uhádli ste!", "white", "on_green"),
                             f"Tajný kód bol {colored(''.join(kod), 'white', 'on_green')}.", end='\n')
                hrat_znovu()
                break

            pokus += 1
        else:
            # Prehra po 10. pokuse.
            padded_print('\n', colored("GAME OVER! Neuhádli ste po 10. pokuse.", "white", "on_red"),
                         f"Tajný kód bol {colored(''.join(kod), 'white', 'on_green')}.", end='\n')
            hrat_znovu()


if __name__ == "__main__":
    zacni_hru()
