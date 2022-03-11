# Mastermind (vo funkcionálnom štýle)

# Jednoduchá hra bežiaca v termináli
# Cieľom hry je uhádnuť náhodný 4-číselný kód
# Na uhádnutie kódu má hráč 10 pokusov
# Po každom pokuse získa informácie, ktoré mu pomôžu logicky prísť na správny kód

# Ak sa číslica v kóde nenachádza, zmení sa na 'Z' ('Zle')
# Ak sa číslica v kóde nachádza, no na inej pozícii, zmení sa na 'P' ('Pozícia')
# Ak sa číslica v kóde nachádza, a je na správnej pozícii, zmení sa na 'S' ('Správne')

import random

def vygeneruj_kod():
    return tuple(random.randint(0, 9) for _ in range(4))


def ziskaj_vstup(pokus):
    print(f"Zadajte 4-číselný kód: (pokus {pokus})\n")
    vstup = input()
    
    # Ak vstup nie je v správnom formáte, zavoláme funkciu znovu
    if len(vstup) != 4 or not vstup.isnumeric():
        print("Vstup musí byť 4-číselný kód, napr. 2005.\n")
        return ziskaj_vstup(pokus)
        
    # Vstup si zmeníme na tuple čísel a vrátime ho
    return tuple(int(i) for i in vstup)


def hrat_znovu():
    print("Chcete hrať znovu? (áno / nie)")
    return input().lower() in ('ano', 'áno', 'a')
  
    
def hraj():
    print("\nMASTERMIND\n",
          "Pravidlá hry:\n",
          "Cieľom hry je uhádnuť náhodný 4-číselný kód.",
          "Na uhádnutie kódu máte 10 pokusov.",
          "Ak sa číslica v kóde nenachádza, zmení sa na 'Z' ('Zle').",
          "Ak sa číslica v kóde nachádza, no na inej pozícii, zmení sa na 'P' ('Pozícia').",
          "Ak sa číslica v kóde nachádza, a je na správnej pozícii, zmení sa na 'S' ('Správne').", sep='\n', end='\n\n')

    kod = vygeneruj_kod()
    str_kod = ''.join(map(str, kod))
    
    def porovnaj(pokus=1):
        if pokus == 11:
            print("GAME OVER!\n\n" +
                  "Kód ste neuhádli po 10. pokuse.\n" +
                  f"Správny kód bol {str_kod}.\n")
            return hraj() if hrat_znovu() else None
        
        vstup = ziskaj_vstup(pokus)
        
        if vstup == kod:
            print(f"Uhádli ste! Tajný kód je {str_kod}.\n")
            return hraj() if hrat_znovu() else None
        
        vystup = ('S' if i == j
                  else 'P' if i in kod
                  else 'Z'
                  for i, j in zip(vstup, kod))
        
        print(''.join(vystup), "\n")
        porovnaj(pokus + 1)
        
    porovnaj()
   
    
if __name__ == "__main__":
    hraj()