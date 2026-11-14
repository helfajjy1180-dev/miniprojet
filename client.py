class client :
    def __init__ (self,id , nom ,email):
        self.id = id
        self.nom = nom
        self.email = email

    def __str__(self):
        return f"Client ID: {self.id}, Name: {self.nom}, Email: {self.email}"