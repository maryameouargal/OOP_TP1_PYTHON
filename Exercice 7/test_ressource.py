import gc
from ressource import Ressource


r1 = Ressource("Base de données")
r1.utiliser()

# suppression explicite de la référence
del r1

# on force le garbage collector 
gc.collect()

print(" Création d'un objet hors portée")

# ici, l'objet est créé sans être gardé dans une variable
Ressource("Fichier temporaire").utiliser()

