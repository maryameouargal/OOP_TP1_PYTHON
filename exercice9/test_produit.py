from produit import Produit

# 1) création et comparaison
p1 = Produit("Stylo", 1.5, 20, ["bureau", "écriture"])
p2 = Produit("Stylo", 1.5, 20, ["bureau", "écriture"])

print(p1)                
print(p1 == p2)           
print(p1.valeur_totale()) 

# 2) valeur par défaut
p3 = Produit("Cahier", 2.0)
print(p3.tags)            # []

# 3) preuve que les listes ne sont pas partagées
p4 = Produit("Gomme", 0.8)
p4.tags.append("scolaire")
print(p3.tags)           
print(p4.tags)           