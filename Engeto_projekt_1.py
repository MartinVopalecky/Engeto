

"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Martin Vopalecky
email: mvopale@email.cz
discord: martin_21315
"""

from task_template import TEXTS

#pocita delka slov
def spocitej_a_vypis_delky_slov(cistena_slova):
      delky_slov = []
      for i in range(100):
            delky_slov.insert(i, 0)  #vytvoří seznam kde pozice je délka slova, hodnota pak počet slov s danou délkou

      for slovo in cistena_slova:
            delky_slov[len(slovo)] += 1  #přičítá délky jednotlivých slov

      for delka in range(100):
            if delky_slov[delka] > 0 :   #pokud se vyskytuje slovo dané délky vypíše graf a počet
                  graf = (delky_slov[delka]*"*")
                  print(str(delka).rjust(2), "|  ", graf, delky_slov[delka] )


def vypocte_pocty_slov(slova): 
      pocet_Titlecase = 0
      pocet_velkymi = 0
      pocet_malymi = 0
      for slovo in slova:
            if str(slovo).istitle():
                  pocet_Titlecase += 1

            elif str(slovo).isupper():
                  pocet_velkymi += 1

            elif str(slovo).islower():
                  pocet_malymi += 1

      return pocet_Titlecase, pocet_velkymi, pocet_malymi   


def spocte_cisla_v_textu(slova):
      #spocte čísla v textu
      soucet = 0
      pocet = 0
      for slovo in slova:
            if str(slovo).isnumeric():
                  pocet +=1
                  soucet += int(slovo)       
      return pocet, soucet


def vycisti_slova(zvoleny_text):
      for slovo in zvoleny_text:
            ciste_slovo = slovo.strip(",.:?;!")
            vycistena_slova.append(ciste_slovo)
      return vycistena_slova


def zjisti_variantu_txt(name):
      print(oddelovac)
      print("Welcome to the app, ", name)
      print("We have 3 texts to be analyzed.")
      print(oddelovac)

      while True:
            var = input("Enter a number btw. 1 and 3 to select: ")
            if var.isdigit() and int(var) >= 1 and int(var) <=3 :
                  break
           
      return int(var) - 1


def zaverecny_tisk():
      print(oddelovac)
      print(f"There are {len(vycistena_slova)} words in the selected text.")
      print(f"There are {pocet_Titlecase} titlecase words.")     
      print(f"There are {pocet_velkymi} uppercase  words.")  
      print(f"There are {pocet_malymi} lowercase words.")          
      print(f"There are {pocet} numeric strings.") 
      print(f"The sum of all the numbers {soucet}")
      print(oddelovac)
      print("LEN|  OCCURENCES ")
      print(oddelovac)



#program ----------------------------------------------------------------------
oddelovac = 40*"-"
vycistena_slova = []
uzivatel = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":\
            "pass123"}

jmeno = input("username: ")
heslo = input("password: ")

if uzivatel.get(jmeno) == heslo:   
    varianta = zjisti_variantu_txt(jmeno) #uživatel vybere jednu variantu ze 3

else:
    print("unregistered user, terminating the program..")
    exit()


zvoleny_text = TEXTS[varianta].split()  
#ocisti slova od specialnich znaku jako ",.:?;!"
vycistena_slova = vycisti_slova(zvoleny_text) 

pocet_Titlecase, pocet_velkymi, pocet_malymi = vypocte_pocty_slov(\
      vycistena_slova)

pocet, soucet = spocte_cisla_v_textu(vycistena_slova)

zaverecny_tisk()

spocitej_a_vypis_delky_slov(vycistena_slova) #vypíše graf a počty délek slov


