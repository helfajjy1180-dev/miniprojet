import mysql.connector
from produit import Produit
from client import client


class MySQLDAO:


    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="hayathayat12..",
            database="mini_projet"
        )

        self.cursor = self.conn.cursor()

    def ajouter_produit(self, produit):
        self.cursor.execute(
            "INSERT INTO produits VALUES (%s, %s, %s)",
            (produit.id, produit.nom, produit.prix)
        )
        self.conn.commit()

    def lister_produits(self):
        self.cursor.execute("SELECT * FROM produits")
        lignes = self.cursor.fetchall()

        return [
            Produit(id, nom, prix)
            for id, nom, prix in lignes
        ]

    def ajouter_client(self, client):
        self.cursor.execute(
            "INSERT INTO clients VALUES (%s, %s, %s)",
            (client.id, client.nom, client.email)
        )
        self.conn.commit()

    def lister_clients(self):
        self.cursor.execute("SELECT * FROM clients")
        lignes = self.cursor.fetchall()

        return [
            client(id, nom, email)
            for id, nom, email in lignes
        ]

    def rechercher_client(self, email):
        self.cursor.execute(
            "SELECT * FROM clients WHERE email = %s",
            (email,)
        )

        ligne = self.cursor.fetchone()

        if ligne:
            return client(*ligne)

        return None

    def modifier_prix(self, id_produit, nouveau_prix):
        self.cursor.execute(
            "UPDATE produits SET prix = %s WHERE id = %s",
            (nouveau_prix, id_produit)
        )
        self.conn.commit()

    def fermer(self):
        self.cursor.close()
        self.conn.close()