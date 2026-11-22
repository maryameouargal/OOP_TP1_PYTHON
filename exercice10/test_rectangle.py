from validateurs import Rectangle

rect = Rectangle(4, 6)

# 1) appel normal
print(rect.aire())         

# 2) avec un facteur valide
print(rect.aire(2.5))      

# 3) facteur invalide 
try:
    rect.aire(-2)
except ValueError as e:
    print(f"Refusé : {e}")

# 4) facteur invalide
try:
    rect.aire("grand")
except ValueError as e:
    print(f"Refusé : {e}")