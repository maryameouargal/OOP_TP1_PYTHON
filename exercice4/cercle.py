import math


class Cercle:
    def __init__(self, rayon: float):
        # on passe par la propriété : le setter vérifie la valeur
        self.rayon = rayon

    @property
    def rayon(self):
        """Renvoie la valeur actuelle du rayon."""
        return self._rayon

    @rayon.setter
    def rayon(self, valeur: float):
        """Vérifie que le rayon est valide avant de l'enregistrer."""
        if valeur <= 0:
            raise ValueError("Un rayon doit être plus grand que zéro.")
        self._rayon = valeur

    def aire(self) -> float:
        return math.pi * self.rayon ** 2

    def perimetre(self) -> float:
        return 2 * math.pi * self.rayon

    def __str__(self):
        return f"<Cercle de rayon {self.rayon}>"