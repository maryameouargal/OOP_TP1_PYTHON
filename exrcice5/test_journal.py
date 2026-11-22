from journal import JournalTaches

with JournalTaches("taches_demo.txt") as journal:
    journal.ajouter_tache("Relire le cours sur les classes")
    journal.ajouter_tache("Terminer l'exercice quatre!!!!!!")

# le fichier est refermé automatiquement ici

# on vérifie ce qui a été écrit
with open("taches_demo.txt", "r", encoding="utf-8") as f:
    print(f.read())

# tentative d'écriture hors du bloc with
journal_ferme = JournalTaches("taches_demo.txt")
try:
    journal_ferme.ajouter_tache("Cette ligne ne doit pas s'écrire")
except RuntimeError as e:
    print(f"Refusé : {e}")