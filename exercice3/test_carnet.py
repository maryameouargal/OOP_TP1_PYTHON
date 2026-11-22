from contact import Contact
from carnet import Carnet

carnet = Carnet()
c1 = Contact("Rina Knet", "0616767668", "rina@exam.com")
c2 = Contact("Be joy", "0698444432", "beee@example.com")
carnet.ajouter(c1)
carnet.ajouter(c2)

print(c1.initiale)          
resultats = carnet.chercher("ri")
print(resultats)            
print(len(carnet))          