class Ressource:
    def __init__(self, nom: str):
        self.nom = nom
        print(f"[INIT] Ressource '{nom}' créée")

    def __del__(self):
        # appelé quand l'objet est détruit
        print(f"[DELETEE] Ressource '{self.nom}' supprimée")

    def utiliser(self):
        print(f"[USE] Utilisation de '{self.nom}'")