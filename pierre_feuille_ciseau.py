import random


arret_de_la_partie=False

while arret_de_la_partie == False:
    print("Pierre feuille ciseaux\n")
    choice = input("Entrez un choix entre pierre, feuille ou ciseaux : ")
    print("Vous avez pris " + choice)
    signes_collection = ["pierre", "feuille", "ciseaux"]
    computer_choice = random.choice(signes_collection)
    print("L'ordinateur a choisit " + computer_choice + "!")

    if computer_choice == choice:
        print("égalité")


    if choice == "ciseaux":
        if computer_choice == "feuille":
            print("Les ciseaux coupent la feuille, vous avez gagné!")
        else:
            print("La pierre casse le ciseau, vous avez perdu!")
    elif choice == "feuille":
        if computer_choice == "pierre":
            print("La feuille couvre la pierre, vous avez gagné!")
        else:
            print("Les ciseaux coupent la feuille, vous avez perdu!")
    elif choice == "pierre":
        if computer_choice == "ciseaux":
            print("La pierre casse le ciseau, vous avez gagné!")
        else:
            print("La feuille couvre la pierre, vous avez perdu!")
    else:
        pass

    fin_de_la_partie = input("Souhaitez-vous arrêter la partie? (O/N) : ")

    if fin_de_la_partie == "O" or fin_de_la_partie == "o":
        arret_de_la_partie = True
    elif fin_de_la_partie == "N" or fin_de_la_partie == "n":
        arret_de_la_partie = False
