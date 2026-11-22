from dataclasses import dataclass, field
from typing import List


@dataclass
class Produit:
    nom: str
    prix: float
    quantite: int = 0
    # default_factory 
    tags: List[str] = field(default_factory=list)

    def valeur_totale(self) -> float:
        # calcul simple : prix unitaire * quantité
        return self.prix * self.quantite