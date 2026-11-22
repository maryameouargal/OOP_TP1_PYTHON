from convertisseur import Convertisseur

# 1) appel direct sur la classe, sans instance
print(Convertisseur.vers_dh(800))         

# 2) on change le taux
Convertisseur.changer_taux(11.2)
print(Convertisseur.depuis_dh(112))      

# 3) avec une instance
conv = Convertisseur()
print(conv.vers_dh(34))                 

# 4) tentative de taux invalide
try:
    Convertisseur.changer_taux(0)
except ValueError as e:
    print(f"Refusé : {e}")