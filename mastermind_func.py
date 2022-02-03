import random

def vygeneruj_kod():
    return [random.randint(0, 9) for _ in range(4)]


def ziskaj_vstup(krok):
    print(f"Zadajte 4-číselný kód: (pokus {krok})\n")
    vstup = input()
    
    # Ak vstup nie je v správnom formáte, zavoláme funkciu znovu
    if len(vstup) != 4 or not vstup.isnumeric():
        print("Vstup musí byť 4-číselný kód, napr. 1234.\n")
        return ziskaj_vstup(krok)
        
    # Vstup si zmeníme na pole čísel
    return [int(i) for i in vstup]


def hrat_znovu():
    print("Chcete hrať znovu? (áno / nie)")
    if (input().lower() in ['ano', 'áno', 'a']):
        hraj()
  
    
def hraj():
    print("\nMASTERMIND\n\n"
          "Pravidlá hry:\n\n"
          "Cieľom hry je uhádnuť náhodný 4-číselný kód.\n"
          "Na uhádnutie kódu máte 10 pokusov.\n"
          "Ak sa číslica v kóde nenachádza, zmení sa na 'Z'.\n"
          "Ak sa číslica v kóde nachádza, no na inej pozícii, zmení sa na 'P'.\n"
          "Ak sa číslica v kóde nachádza, a je na správnej pozícii, zmení sa na 'S'.\n")

    kod = vygeneruj_kod()
    str_kod = ''.join(map(str, kod))
    
    def porovnaj(krok=1):
        if krok == 11:
            print("GAME OVER!\n\n" +
                  "Kód ste neuhádli po 10. pokuse.\n" +
                  f"Správny kód bol {str_kod}.\n")
            hrat_znovu()
            return
        
        vstup = ziskaj_vstup(krok)
        
        if vstup == kod:
            print(f"Uhádli ste! Tajný kód je {str_kod}.\n")
            hrat_znovu()
            return
        
        vystup = ['S' if i == j
                  else 'P' if i in kod
                  else 'Z'
                  for i, j in zip(vstup, kod)]
        
        print(''.join(vystup), "\n")
        porovnaj(krok + 1)
        
    porovnaj()
   
    
if __name__ == "__main__":
    hraj()