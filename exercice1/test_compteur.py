from compteur_page import CompteurPage

# Création de deux pages
page1 = CompteurPage("Accueil")
page2 = CompteurPage("Contact")

# Ajout de visites
page1.ajouter_visite()
page1.ajouter_visite()
page2.ajouter_visite()

# Affichage
print(page1.afficher_statistiques())  
print(page2.afficher_statistiques())  
print(CompteurPage.total_visites)     