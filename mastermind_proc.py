import random

krok = 1
dalsia_hra = True

def vygeneruj_kod():
    kod = []
    for i in range(4):
        kod.append(random.randint(0, 9))
    return kod


def ziskaj_vstup():
    print(f"Zadajte 4-číselný kód: (pokus {krok})\n")
    vstup = input()
    
    while(len(vstup) != 4 or not vstup.isnumeric()):
        print("Vstup musí byť 4-číselný kód, napr. 1234.\n")
        print(f"Zadajte 4-číselný kód: (pokus {krok})\n")
        vstup = input()

    # Vstup si zmeníme na pole čísel
    int_vstup = []
    for i in vstup:
        int_vstup.append(int(i))
        
    return int_vstup


def hrat_znovu():
    print("Chcete hrať znovu? (áno / nie)")
    global dalsia_hra
    dalsia_hra = input().lower() in ['ano', 'áno', 'a']
  
    
def hraj():
    while(dalsia_hra):
        print("\nMASTERMIND\n\n"
          "Pravidlá hry:\n\n"
          "Cieľom hry je uhádnuť náhodný 4-číselný kód.\n"
          "Na uhádnutie kódu máte 10 pokusov.\n"
          "Ak sa číslica v kóde nenachádza, zmení sa na 'Z'.\n"
          "Ak sa číslica v kóde nachádza, no na inej pozícii, zmení sa na 'P'.\n"
          "Ak sa číslica v kóde nachádza, a je na správnej pozícii, zmení sa na 'S'.\n")
        
        global krok
        krok = 1
        kod = vygeneruj_kod()
        
        str_kod = ""
        for i in kod:
            str_kod += str(i)
        
        while krok <= 10:
            vstup = ziskaj_vstup()
            
            if vstup == kod:
                print(f"Uhádli ste! Tajný kód je {str_kod}.\n")
                hrat_znovu()
                break
            
            vystup = ""
            
            for i in range(len(vstup)):
                if vstup[i] in kod:
                    if vstup[i] == kod[i]:
                        vystup += "S"
                    else: vystup += "P"
                else: vystup += "Z"
                
            print(vystup, "\n")
            krok += 1
        else:    
            print("GAME OVER!\n\n" +
                  "Kód ste neuhádli po 10. pokuse.\n" +
                  f"Správny kód bol {str_kod}.\n")
            hrat_znovu()


if __name__ == "__main__":
    hraj()