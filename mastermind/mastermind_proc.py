# Mastermind (v procedurálnom štýle)

# Jednoduchá hra bežiaca v termináli
# Cieľom hry je uhádnuť náhodný 4-číselný kód
# Na uhádnutie kódu má hráč 10 pokusov
# Po každom pokuse získa informácie, ktoré mu pomôžu logicky prísť na správny kód

# Ak sa číslica v kóde nenachádza, zmení sa na 'Z' ('Zle')
# Ak sa číslica v kóde nachádza, no na inej pozícii, zmení sa na 'P' ('Pozícia')
# Ak sa číslica v kóde nachádza, a je na správnej pozícii, zmení sa na 'S' ('Správne')

import random

pokus = 1

def vygeneruj_kod():
    kod = []
    for i in range(4):
        kod.append(random.randint(0, 9))
    return kod


def ziskaj_vstup():
    print(f"Zadajte 4-číselný kód: (pokus {pokus})\n")
    vstup = input()
    
    while(len(vstup) != 4 or not vstup.isnumeric()):
        print("Vstup musí byť 4-číselný kód, napr. 1234.\n")
        print(f"Zadajte 4-číselný kód: (pokus {pokus})\n")
        vstup = input()

    # Vstup si zmeníme na pole čísel
    int_vstup = []
    for i in vstup:
        int_vstup.append(int(i))
        
    return int_vstup


def hrat_znovu():
    print("Chcete hrať znovu? (áno / nie)")
    return input().lower() in ('ano', 'áno', 'a')
  
    
def hraj():
    dalsia_hra = True
    
    while(dalsia_hra):
        print("\nMASTERMIND\n",
          "Pravidlá hry:\n",
          "Cieľom hry je uhádnuť náhodný 4-číselný kód.",
          "Na uhádnutie kódu máte 10 pokusov.",
          "Ak sa číslica v kóde nenachádza, zmení sa na 'Z' ('Zle').",
          "Ak sa číslica v kóde nachádza, no na inej pozícii, zmení sa na 'P' ('Pozícia').",
          "Ak sa číslica v kóde nachádza, a je na správnej pozícii, zmení sa na 'S' ('Správne').", sep='\n', end='\n\n')
        
        global pokus
        pokus = 1
        kod = vygeneruj_kod()
        
        str_kod = ""
        for i in kod:
            str_kod += str(i)
        
        while pokus <= 10:
            vstup = ziskaj_vstup()
            
            if vstup == kod:
                print(f"Uhádli ste! Tajný kód je {str_kod}.\n")
                dalsia_hra = hrat_znovu()
                break
            
            vystup = ""
            for i in range(len(vstup)):
                if vstup[i] in kod:
                    if vstup[i] == kod[i]:
                        vystup += "S"
                    else: vystup += "P"
                else: vystup += "Z"
                
            print(vystup, "\n")
            pokus += 1
        else:    
            print("GAME OVER!\n\n" +
                  "Kód ste neuhádli po 10. pokuse.\n" +
                  f"Správny kód bol {str_kod}.\n")
            dalsia_hra = hrat_znovu()


if __name__ == "__main__":
    hraj()