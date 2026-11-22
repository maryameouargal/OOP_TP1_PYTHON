from vecteur import Vecteur2D

v1 = Vecteur2D(2, 5)
v2 = Vecteur2D(3, 1)

print(v1 + v2)      
print(v2 - v1)      
print(v1 * 3)       

# test de l'égalité
print(v1 == Vecteur2D(2, 5))  
print(v1 == "un texte")        

# test du __hash__
ensemble = {v1, v2}
print(len(ensemble))           