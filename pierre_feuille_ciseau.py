import random


arret_de_la_partie=False

while arret_de_la_partie == False:
    print("Pierre feuille ciseaux\n")
    choice = input("Entrez un choix entre pierre, feuille ou ciseaux : ")
    print("Vous avez pris " + choice)
    signes_collection = ["pierre", "feuille", "ciseaux"]
    rrrr = random.randint(0,2)
    aaaa = signes_collection[rrrr]
    print("L'ordinateur a choisit " + aaaa + "!")

    if aaaa == choice:
        print("égalité")


    if aaaa == "pierre" and choice == "ciseaux":
        print("L'ordinateur a gagné\n")
    elif aaaa == "ciseaux" and choice == "feuille":
        print("L'ordinateur a gagné\n")
    elif aaaa == "feuille" and choice == "pierre":
        print("L'ordinateur a gagné\n")


    elif choice == "pierre" and aaaa == "ciseaux":
        print("Vous avez gagné\n")
    elif choice == "ciseaux" and aaaa == "feuille":
        print("Vous avez gagné\n")    
    elif choice == "feuille" and aaaa == "pierre":
        print("Vous avez gagné\n")


    fin_de_la_partie = input("Souhaitez-vous arrêter la partie? (O/N) : ")

    if fin_de_la_partie == "O" or fin_de_la_partie == "o":
        arret_de_la_partie = True
    elif fin_de_la_partie == "N" or fin_de_la_partie == "n":
        arret_de_la_partie = False
