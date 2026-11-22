class Convertisseur:
    # taux de change EUR -> DH, la meme dans toutes les instances
    taux_eur_dh = 10.9

    @staticmethod
    def vers_dh(euros: float) -> float:
        # méthode statique : ne reçoit pas d'instance 
        return euros * Convertisseur.taux_eur_dh

    @classmethod
    def changer_taux(cls, nouveau_taux: float):
        # méthode de classe : reçoit cls pour modifier le taux
        if nouveau_taux <= 0:
            raise ValueError("Le taux de change doit être supérieur à zéro.")
        cls.taux_eur_dh = nouveau_taux

    @classmethod
    def depuis_dh(cls, dirhams: float) -> float:
        # méthode de classe : lit le taux via cls
        return dirhams / cls.taux_eur_dh