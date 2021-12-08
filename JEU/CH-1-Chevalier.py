#CH-1-Chevalier
from random import *
import classe_personnage_jdr as AA

class histoire_chevalier:

    def __init__(self):

        self.place = 1
        self.prologue = False
        self.choix_moral1 = ""
        self.choix_moral2 = ""
        self.choix_moral3 = ""
        self.fight_debut = False


        
    
    def jeu(self, debut):
        
        while self.place > 0:

            while self.prologue is False:
                
                print("Vous vous réveiller par un bruit de pas ;")
                print("le bruit de pas de gardes royaux au pied de votre porte.")
                print("Vous vous levez, ouvrez la porte et un message vous est tendu : ")
                print("*** Sir, le royaume court un grave danger, ***")
                print("*** les 3 cristaux de Dahal ont été volé à Icegate. ***")
                print("*** Le royaume est tombé dans une nuit éternelle ***")
                print("*** où les monstres peuvent y refaire leur apparition. ***")
                print("*** Par ordre du roi, vous devez les retrouver  ***")
                print("*** et arrêter celui qui les a dérobés… ***")
                print("Vous n'avez pas besoin d'en lire plus, vous saviez que cela allait arriver,")
                print("et vous en savez le danger, mais vous vous rappelez également")
                print("vos mauvaises relations récentes avec le Roi. Vous devez prendre une décision.")
                while self.choix_moral1 != "accepter l'ordre" and self.choix_moral1 != "refuser l'ordre" :
                    self.choix_moral1 = input("Que faites vous ? (accepter l'ordre/ refuser l'ordre) ")
                    self.choix_moral1 = self.choix_moral1.lower()

                if self.choix_moral1 == "accepter l'ordre" :
                    self.fight_debut = True
                else:
                    self.fight_debut = AA.fight_Refus()
                print("")
                if self.fight_debut is False:
                    self.place = 0
                else:
                    if self.choix_moral1 == "accepter l'ordre" :
                        print("Vous avez décidé de laisser mécontentement envers le Roi de côté")
                        print("et accepter la mission. Les gardes repartent et vous partez en")
                        print("route vers la clairrière au centre du royaume.")
                        print("")
                        print("")
                        print("Vous arrivez dans la clairrière, lieu habituellement plein de vie")
                        print("Où toutes les histoires ce raconte. Mais seul quelques personnes")
                        print("Passe de temps en temps; vous devez essayer de savoir si des rumeurs")
                        print("circulent autours d'un voleur ou des crystaux.")
                        self.place = 1
                    else:
                        print("")
                    
                    self.prologue = True

            
            while self.place == 1 : #aller clairrière
                choix = ""
                while (choix != "interriger un passant" and choix != "prendre un chemin au hazard"):
                    choix = input("Que faites vous ? ( interroger un passant/ prendre un chemin au hazard)")
                    choix = choix.lower()
                if choix == "interroger un passant" :
                    print("")
                    print("Vous interpellez une personne passant à côté de vous")
                    print("et lui demander si elle sait quelque chose : ")
                    print("Après un court échange et une longue réflexion, ")
                    print("Vous apprenez qu'une histoire circule disant")
                    print("que les crystaux ne se trouveraient plus à Icegate")
                    self.place = 2
                elif choix == "prendre un chemin au hazard":
                    print("")
                    print("Ne croisant que peu de personnes, vous décidez de prendre")
                    print("au hazard un des nombreux chemins partants de la clairrière.")
                    print("Vous arrivez dans la contrée de starhill lieu où peu de gens")
                    print("se rende en raison du peu d'intérêt de cette région,")
                    print("mais s'est également ici qu'habite un de vos ami.")
                    self.place = 3

            while self.place == 2 : #demander passant
                choix = ""
                while (choix != "se rendre à Icegate" and choix != "interroger une autre personne"):
                    choix = input("Que faites vous ? ( se rendre à Icegate/ interroger une autre personne")
                    choix = choix.lower()
                if choix == "se rendre à Icegate" :
                    print("")
                    self.place = 4
                elif choix == "interroger une autre personne" :
                    print("")
                    self.place = 5

            while self.place == 3: #chemin hazard(Starhill)
                choix = ""
