import random

from ennemi import Adversaire

class Combat:
    def __init__(self, nom, puissance):
        self.nom = nom
        self.puissance = puissance

attaques = [
    Combat("Vive attaque", 10),
    Combat("Canon à eau", 15),
    Combat("Tsunami", 25)
]

adversaires = [
    Adversaire("pokemon1", 50, 5),
    Adversaire("pokemon2", 75, 10),
    Adversaire("pokemon3", 200, 50)
]

def attaque(adversaire, attaque):
    degats = attaque.puissance - adversaire.defense
    if degats < 0:
        degats = 0
    adversaire.pv -= degats
    return degats

def combat():
    adversaire = random.choice(adversaires)
    print("Un", adversaire.nom, "s'approche!")
    while adversaire.pv > 0:
        print(adversaire.nom, ":", adversaire.pv, "PV")
        print("1. Vive attaque (10 de puissance)")
        print("2. Canon à eau (15 de puissance)")
        print("3. Tsunami (25 de puissance)")
        choix = input("Choisissez une attaque: ")
        attaque_choisie = attaques[int(choix) - 1]
        degats = attaque(adversaire, attaque_choisie)
        print("Vous infligez", degats, "points de dégâts à", adversaire.nom)
        if adversaire.pv <= 0:
            print("Vous avez vaincu", adversaire.nom)
            break
        degats = attaque(adversaire, random.choice(Combats))
        print(adversaire.nom, "vous inflige", degats, "points de dégâts!")
        if adversaire.pv <= 0:
            print("Vous avez été vaincu par", adversaire.nom)

combat()
