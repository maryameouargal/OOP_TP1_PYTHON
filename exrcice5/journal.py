class JournalTaches:
    def __init__(self, nom_fichier: str = "journal.txt"):
        self.nom_fichier = nom_fichier
        self.fichier = None

    def __enter__(self):
        # début du bloc with : on ouvre le fichier en ajout
        self.fichier = open(self.nom_fichier, "a", encoding="utf-8")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # fin du bloc with  on referme le fichier, même si une erreur est survenue
        if self.fichier is not None:
            self.fichier.close()
        # False = on laisse remonter les exceptions éventuelles
        return False

    def ajouter_tache(self, description: str):
        # on refuse d'écrire si le journal n'a pas été ouvert via with
        if self.fichier is None:
            raise RuntimeError("Journal fermé : ouvrez-le avec 'with'.\n")
        self.fichier.write(f"- {description}\n")