from cercle import Cercle

c = Cercle(3.5)

print(f"Aire      : {c.aire():.2f}")       
print(f"Périmètre : {c.perimetre():.2f}")   
print(c)                                  

try:
    c.rayon = 0
except ValueError as e:
    print(f"Refusé : {e}")               