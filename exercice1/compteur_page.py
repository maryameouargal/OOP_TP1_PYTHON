class CompteurPage:
    # Attribut de classe 
    total_visites = 0

    def __init__(self, nom_page):
        # Attribut d'instance 
        self.nom_page = nom_page
        self.visites = 0
        CompteurPage.total_visites += 1

    def ajouter_visite(self):
        self.visites += 1
        CompteurPage.total_visites += 1

    def afficher_statistiques(self):
        return (f"Page '{self.nom_page}': {self.visites} visites. "
                f"Total global: {CompteurPage.total_visites}")