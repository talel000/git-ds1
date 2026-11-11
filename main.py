# Version 1.0 - Gestion des taches
taches = []

while True:
    print(" GESTION DES TACHES ")
    print("1. Ajouter une tache")
    print("2. Afficher les taches")
    print("3. Rechercher une tache")
    print("0. Quitter")

    choix = input("Votre choix : ")


    if choix == "1":
        titre = input("Entrez le titre de la tache : ")
        if titre == "":
            print("Erreur : Le titre ne peut pas etre vide.")
        else:
            taches.append(titre)
            print("Tache ajoutee avec succes.")

    elif choix == "2":
        if len(taches) == 0:
            print("La liste des taches est vide.")
        else:
            print(" Liste des taches ")
            numero = 1
            for tache in taches:
                print(numero, "-", tache)
                numero = numero + 1


    elif choix == "3":
        if len(taches) == 0:
            print("La liste est vide.")
        else:
            mot_cle = input("Entrez le mot-cle a rechercher : ")
            trouve = False
            numero = 1
            for tache in taches:
                if mot_cle in tache:
                    print(numero, "-", tache)
                    trouve = True
                numero = numero + 1
            if not trouve:
                print("Aucune tache ne contient ce mot-cle.")

    elif choix == "0":
        print("Fin du programme. Au revoir !")
        break


    else:
        print("Erreur : Choix invalide, veuillez taper 1, 2, 3 ou 0.")