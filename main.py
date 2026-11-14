
from produit import Produit
from client import client
from sqlite_dao import SQLiteDAO
from mysql_dao import MySQLDAO


def afficher_menu():
    print("\n========== GESTION BOUTIQUE ==========")
    print("1. Ajouter un produit")
    print("2. Lister les produits")
    print("3. Modifier le prix d'un produit")
    print("4. Ajouter un client")
    print("5. Lister les clients")
    print("6. Rechercher un client par email")
    print("0. Quitter")
    print("======================================")


def main():

    print("Choisir la base de données :")
    print("1. SQLite")
    print("2. MySQL")

    choix = input("Votre choix : ")

    try:
        if choix == "1":
            dao = SQLiteDAO()
            print("Connexion SQLite réussie.")

        elif choix == "2":
            dao = MySQLDAO()
            print("Connexion MySQL réussie.")

        else:
            print("Choix invalide.")
            return

        while True:

            afficher_menu()
            choix = input("Votre choix : ")

            try:
                if choix == "1":
                    nom = input("Nom du produit : ")
                    prix = float(input("Prix : "))

                    produit = Produit(None, nom, prix)
                    dao.ajouter_produit(produit)

                    print("Produit ajouté avec succès.")

                elif choix == "2":
                    produits = dao.lister_produits()

                    for p in produits:
                        print(p)

                elif choix == "3":
                    id = int(input("ID du produit : "))
                    prix = float(input("Nouveau prix : "))

                    dao.modifier_prix(id, prix)
                    print("Prix modifié avec succès.")

                elif choix == "4":
                    nom = input("Nom du client : ")
                    email = input("Email du client : ")

                    client = client(None, nom, email)
                    dao.ajouter_client(client)

                    print("Client ajouté avec succès.")

                elif choix == "5":
                    clients = dao.lister_clients()

                    for c in clients:
                        print(c)

                elif choix == "6":
                    email = input("Email à rechercher : ")

                    client = dao.rechercher_client(email)

                    if client:
                        print(client)
                    else:
                        print("Client introuvable.")

                elif choix == "0":
                    print("Fin du programme.")
                    break

                else:
                    print("Choix invalide.")

            except (ValueError, Exception) as e:
                print("Erreur :", e)

        dao.fermer()

    except Exception as e:
        print("Erreur de connexion à la base de données :", e)


if __name__ == "__main__":
    main()
