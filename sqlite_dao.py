
import sqlite3
from produit import Produit
from client import client


class SQLiteDAO:

    def __init__(self):
        self.conn = sqlite3.connect("boutique.db")
        self.creer_tables()

    def creer_tables(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prix REAL NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)

        self.conn.commit()

    # Ajouter un produit
    def ajouter_produit(self, produit):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO produits (nom, prix) VALUES (?, ?)",
            (produit.nom, produit.prix)
        )
        self.conn.commit()

    # Lister les produits
    def lister_produits(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM produits")
        lignes = cursor.fetchall()

        return [
            Produit(id, nom, prix)
            for id, nom, prix in lignes
        ]

    # Ajouter un client
    def ajouter_client(self, client):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO clients (nom, email) VALUES (?, ?)",
            (client.nom, client.email)
        )
        self.conn.commit()

    # Lister les clients
    def lister_clients(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM clients")
        lignes = cursor.fetchall()

        return [
            client(id, nom, email)
            for id, nom, email in lignes
        ]

    # Rechercher un client par email
    def rechercher_client(self, email):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM clients WHERE email = ?",
            (email,)
        )

        ligne = cursor.fetchone()

        if ligne:
            return Client(*ligne)

        return None

    # Modifier le prix d'un produit
    def modifier_prix(self, id, nouveau_prix):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE produits SET prix = ? WHERE id = ?",
            (nouveau_prix, id)
        )
        self.conn.commit()

    # Fermer la connexion
    def fermer(self):
        self.conn.close()
