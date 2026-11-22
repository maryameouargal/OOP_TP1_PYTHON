class Article:
    def __init__(self, reference: str, designation: str, prix_ht: float, stock: int):
        self.reference = reference
        self.designation = designation
        self.prix_ht = prix_ht
        self.stock = stock

    def valeur_stock(self) -> float:
        #Calculate the total value of the stock for an article
        return self.prix_ht * self.stock

    def ajouter_stock(self, quantite: int):
        #add stock to the article, ensuring that the quantity is not negative
        if quantite < 0:
            raise ValueError("la quantite ajoutée ne peut pas être négative.")
        self.stock += quantite

    def __str__(self):
        return (f"[{self.reference}] {self.designation} - "
                f"Stock: {self.stock} - Prix HT: {self.prix_ht:.2f}")