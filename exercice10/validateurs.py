import functools


def valider_positif(*indices: int):
    """Décorateur qui vérifie que les arguments ciblés sont bien des nombres positifs."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for idx in indices:
                # on vérifie seulement si l'argument existe à cet indice
                if idx < len(args):
                    valeur = args[idx]
                    if not isinstance(valeur, (int, float)) or valeur <= 0:
                        raise ValueError(
                            f"Valeur invalide à l'indice {idx} : "
                            f"{valeur} (il faut un nombre > 0)."
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorator


class Rectangle:
    def __init__(self, largeur: float, hauteur: float):
        self.largeur = largeur
        self.hauteur = hauteur

    # self = index 0, facteur = index 1
    @valider_positif(1)
    def aire(self, facteur: float = 1.0) -> float:
        return self.largeur * self.hauteur * facteur