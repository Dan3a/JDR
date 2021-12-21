# Copyright (c) 2021, Dan3A, rremi0     <21985756+Dan3a@users.noreply.github.com>

# This file is part of Crystal Quest.

#     Crystal Quest is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     Crystal Quest is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with Crystal Quest.  If not, see https://www.gnu.org/licenses/. 

from random import randrange

personnage = "chevalier"
sdes = 12

class Perso:

    def __init__(self):

        #global
        self.name = ""
        self.force = 30
        self.ruse = 1
        self.eloquence = 1
        self.attaque = 1
        self.armure = 1
        self.pouvoir = 1
        self.pv_physique = 30
        self.pv_mental = 10 
        self.etat = ""
        self.vitesse = 0
        self.PO = 50
        self.arme = []
        self.armure = []
        self.sort = []
        #Armes [degats, prix, nombre, force mini]
        self.Armes = {"dague":[4, 5, 1, 1], "épée":[10, 15, 0, 1], "masse":[15, 20, 0, 5], "fléau":[18, 25, 0, 1],
                        "Master_Sword":[35, 50, 0, 1], "Mjölnir":[42, 70, 0, 1], "FROSTMOURNE":[50, 0, 0, 1]}
        #Armures [protection, prix, nombre, force mini]
        self.Armures = {
            "gambison de cuir":[1, 10, 0, 1], 
            "armure de fer":[3, 30, 0, 3], 
            "armure d'acier":[4, 40, 0, 5],
            "armure ancestrale":[10, 60, 0, 7], 
            "bouclier hylien":[20, 80, 0, 10], 
            "daedrique":[60, 0, 0, 20]}

    #REPARTITION DES CARACTERISTIQUE DES PERSONNAGE AU DEBUT DE LA PARTIE
    def debut(self, mainWindow):
        self.mainWindow = mainWindow
        self.name = self.mainWindow.waitForEntryText("Quel est votre nom ? : ")
        self.pv_physique = 30
        self.pv_mental = 10
        self.force = 5
        self.eloquence = 10
        self.ruse = 5
        self.attaque = 5
        self.armure = 5
        self.pouvoir = 0
        self.argent = 20

    #SELECTION DES ARMES, ARMURES, ET SORTS LORS DE LA PARTIE
    def selection(self, arme, armure):

        choix = ""
        #choix des armes
        if arme is True:
            while (choix in self.Armes) == False:
                choix = self.mainWindow.waitForEntryText("Choix d'arme : ")
                choix = choix.lower()
                
            
            if (self.Armes[choix][2] > 0 and self.Armes[choix][3] <= self.force):
                self.arme = self.Armes[choix]

        #choix des armures
        if armure is True:
            while (choix in self.Armures) == False:
                choix = self.mainWindow.waitForEntryText("Choix d'armure : ")
                choix = choix.lower()
            if (self.Armures[choix][2] > 0 and self.Armures[choix][3] <= self.force):
                self.armure = self.Armures[choix]
            

    #PREMIERE PARTIE DE L'INVENTAIRE DES PERSONNAGES
    def inventaire(self) :

        ratio = float(self.pv_physique)+float(self.pv_mental)
        if ratio == 30.0 :
            self.etat = " est en pleine forme"
        elif ratio >= 25.0 :
            self.etat = " est en forme"
        elif ratio >= 20 :
            self.etat = " a quelques blessures superficielles"
        elif ratio >= 12 :
            self.etat = " est blessé et a besoin de soins"
        else :
            self.etat = " est gravement blessé"
        self.mainWindow.printInTextArea (self.name,self.etat)

        self.mainWindow.printInTextArea("### Argent : ",self.argent," pièces d'or")

        self.mainWindow.printInTextArea("### Force  : ",self.force)

        self.mainWindow.printInTextArea("### Ruse   : ",self.ruse)

        self.mainWindow.printInTextArea("### Vie      : ",self.pv_physique)

        self.mainWindow.printInTextArea("Inventaire :")

        for key,nb in self.Armes.items() :
            if nb[2] > 0 :
                self.mainWindow.printInTextArea ("- ",nb[2]," ",key)
        for key,nb in self.Armures.items() :
            if nb[2] > 0 :
                self.mainWindow.printInTextArea ("- ",nb[2]," ",key)
        self.mainWindow.printInTextArea("")

    #DEFINITION DES DIFFERENTS MODULES DES COMBATS
    def fight(self, nom, att, ca, vit, dex, pv, distance) :
        
        nb_recul = 1
        nb_recul_m = 2
        self.inventaire()
        self.selection(True,True,False)
        self.mainWindow.printInTextArea ("Un ",nom," attaque")
        while pv > 0 and self.pv_physique > 0 :
            self.inventaire()
            self.mainWindow.printInTextArea("Le",nom,"est à ",distance," mètres de distance. Il a ",pv," pv")
            choix = ""
            while (choix != "avancer" and choix != "reculer" and choix != "rien"
                   and choix != "attaquer" and choix != "sort") :
                choix = self.mainWindow.waitForEntryText("Que faites-vous? (avancer/ reculer/ attaquer/ rien )")
            if choix == "avancer" and distance > self.vitesse :
                distance -= self.vitesse
            elif choix == "avancer" and distance <= self.vitesse :
                distance = 1
            elif choix == "reculer" and nb_recul > 0 :
                nb_recul -= 1
                distance += self.vitesse
            elif choix == "reculer" and nb_recul < 0 :
                self.mainWindow.printInTextArea("Tu ne peux plus reculer")
            elif choix == "attaquer" and distance == 1 :
                self.selection(1,0)
                toucher = randrange(1, 20)
                if toucher <= sdes :
                    pv -= self.arme[0]
                    self.mainWindow.printInTextArea("Tu le frappes et lui inflige" ),self.arme[0]," dégàts"
                else :
                    self.mainWindow.printInTextArea("Tu le rates")
            elif choix == "attaquer" and distance > 1 :
                self.mainWindow.printInTextArea("Impossible tu es trop loin de la cible")
                choix = ""
            else : ()
            if pv <= 0 :
                self.mainWindow.printInTextArea("Tu as vaincu!")
                return True
            else :
                if distance > 1 and att < self.arme[0] and nb_recul_m > 0 :
                    self.mainWindow.printInTextArea("Le",nom,"recule")
                    distance += vit
                    nb_recul_m -= 1
                elif (distance > 1 and att > self.arme[0]) or (distance > 1 and nb_recul_m == 0) :
                    self.mainWindow.printInTextArea("Le",nom,"avance")
                    if vit > distance :
                        distance = 1
                    else :
                        distance -= vit
                elif distance == 1 :
                    toucher = randrange(1, 20)
                    if toucher <= sdes :
                        self.mainWindow.printInTextArea("Il t'attaque et t'inflige ",att," points de dégàts")
                        self.pv_physique -= att
                    else :
                        self.mainWindow.printInTextArea("Il n'arrive pas à te toucher")
        if self.pv_physique <= 0 :
            self.mainWindow.printInTextArea("Il t'a tué!")
            return False
        else :
            return True

    
    def fight_Refus(self) : #combat du début contre les guardes (forcément perdu)
        
        nb_recul = 1
        nb_recul_m = 2
        distance = 5
        pv = 100
        vit = 3
        att = 7
        self.inventaire()
        self.selection(True,True)
        self.mainWindow.printInTextArea ("Les gardes vous attaquent")
        while pv > 0 and self.pv_physique > 0 :
            self.inventaire()
            self.mainWindow.printInTextArea("Les gardes sont à ",distance," mètres de distance. Ils ont ",pv," pv")
            choix = ""
            while (choix != "avancer" and choix != "reculer" and choix != "rien"
                   and choix != "attaquer" and choix != "sort") :
                choix = self.mainWindow.waitForEntryText("Que fais-tu? (avancer/ reculer/ attaquer/ rien )")
            if choix == "avancer" and distance > self.vitesse :
                distance -= self.vitesse
            elif choix == "avancer" and distance <= self.vitesse :
                distance = 1
            elif choix == "reculer" and nb_recul > 0 :
                nb_recul -= 1
                distance += self.vitesse
            elif choix == "reculer" and nb_recul < 0 :
                self.mainWindow.printInTextArea("Tu ne peux plus reculer")
            elif choix == "attaquer" and distance == 1 :
                self.selection(1,0)
                toucher = randrange(1, 20)
                if toucher <= sdes :
                    pv -= self.arme[0]
                    self.mainWindow.printInTextArea("Tu le frappes et lui inflige ",self.arme[0]," dégàts")
                else :
                    self.mainWindow.printInTextArea("Tu le rates")
            elif choix == "attaquer" and distance > 1 :
                self.mainWindow.printInTextArea("Impossible tu es trop loin de la cible")
                choix = ""
            else : ()

            if pv <= 0 :
                self.mainWindow.printInTextArea("Tu as vaincu!")
                return True
            else :
                if distance > 1 and att < self.arme[0] and nb_recul_m > 0 :
                    self.mainWindow.printInTextArea("Les guardes reculent")
                    distance += vit
                    nb_recul_m -= 1
                elif (distance > 1 and att > self.arme[0]) or (distance > 1 and nb_recul_m == 0) :
                    self.mainWindow.printInTextArea("Les gardes avancent")
                    if vit > distance :
                        distance = 1
                    else :
                        distance -= vit
                elif distance == 1 :
                    toucher = randrange(1, 20)
                    if toucher <= sdes :
                        self.mainWindow.printInTextArea("Ils t'attaquent et t'infligent ",att," points de dégàts")
                        self.pv_physique -= att
                    else :
                        self.mainWindow.printInTextArea("Ils n'arrivent pas à te toucher")
        if self.pv_physique <= 0 :
            self.mainWindow.printInTextArea("VOUS ÊTES MORT")
            self.mainWindow.printInTextArea("FIN FUYARDE")
            raise SystemExit(0) 
        else :
            return True

    
    def fight_dernier_gardien(self) : #combat contre le dernier guardien à Icegate
        
        self.mainWindow.printInTextArea("")
        self.mainWindow.printInTextArea("Vous sentez une présence très poche juste derrière vous,")
        self.mainWindow.printInTextArea("Vous distinguez à quelques mètres de vous un homme")
        self.mainWindow.printInTextArea("de votre taille lourdement habillé, il se trouve dans l'ombre")
        self.mainWindow.printInTextArea("et vous ne voyer pas son visage vous aller demander qui il est quand...")
        nb_recul = 1
        nb_recul_m = 2
        distance = 3
        pv = 24
        vit = 4
        att = 6
        sdes1 = 12
        sdes2 = 9
        self.mainWindow.printInTextArea ("Il vous attaque")
        self.inventaire()
        self.selection(True,True)
        while pv > 0 and self.pv_physique > 0 :
            self.inventaire()
            self.mainWindow.printInTextArea("il est à ",distance," mètres de distance. Il a ",pv," pv")
            choix = ""
            while (choix != "avancer" and choix != "reculer" and choix != "rien"
                    and choix != "attaquer" and choix != "sort") :
                choix = self.mainWindow.waitForEntryText("Que fais-tu? (avancer/ reculer/ attaquer/ rien )")
            if choix == "avancer" and distance > self.vitesse :
                distance -= self.vitesse
            elif choix == "avancer" and distance <= self.vitesse :
                distance = 1
            elif choix == "reculer" and nb_recul > 0 :
                nb_recul -= 1
                distance += self.vitesse
            elif choix == "reculer" and nb_recul < 0 :
                self.mainWindow.printInTextArea("Tu ne peux plus reculer")
            elif choix == "attaquer" and distance == 1 :
                self.selection(1,0)
                toucher = randrange(1, 20)
                if toucher <= sdes1 :
                    pv -= self.arme[0]
                    self.mainWindow.printInTextArea("Tu le frappes et lui inflige",self.arme[0],"dégâts")
                else :
                    self.mainWindow.printInTextArea("Tu le rates")
            elif choix == "attaque" and distance > 1 :
                self.mainWindow.printInTextArea("Impossible tu es trop loin de la cible")
                choix = ""
            else : ()


            if pv <= 0 :
                self.mainWindow.printInTextArea("Tu as vaincu!")
                return True
            else :
                if distance > 1 and att < self.arme[0] and nb_recul_m > 0 :
                    self.mainWindow.printInTextArea("Il recule")
                    distance += vit
                    nb_recul_m -= 1
                elif (distance > 1 and att > self.arme[0]) or (distance > 1 and nb_recul_m == 0) :
                    self.mainWindow.printInTextArea("Il avance")
                    if vit > distance :
                        distance = 1
                    else :
                        distance -= vit
                elif distance == 1 :

                    toucher = randrange(1, 50)
                    if toucher <= sdes :
                        self.mainWindow.printInTextArea("Il t'attaque et t'inflige ",att," points de dégàts")
                        self.pv_physique -= att

                    else :
                        self.mainWindow.printInTextArea("Il n'arrive pas à te toucher")
        if self.pv_physique <= 0 :
            self.mainWindow.printInTextArea("Il t'as tué")
            return False
        else :
            return True



    def fight_souterrain1(self) : #combat dans souterrain contre basillic
        
        self.mainWindow.printInTextArea("")
        self.mainWindow.printInTextArea("Quand soudain, les murs de cette immense caverne se mettent à bouger")
        self.mainWindow.printInTextArea("comme une très grande spirale, jusqu'au moment où une tête faisant 5 fois")
        self.mainWindow.printInTextArea("votre taille descend vers vous, une tête au yeux mortels et pleine d'écailles.")
        self.mainWindow.printInTextArea("Le Basillic, ce monstre mythique que toutes les personnes ayant croisé")
        self.mainWindow.printInTextArea("ont finis pétrifiés. Vous restez figé, il s'immobilise jusqu'au moment où...")
        nb_recul = 1
        nb_recul_m = 2
        distance = 10
        pv = 200
        vit = 2
        att = 15
        self.mainWindow.printInTextArea ("Il vous attaque")
        self.inventaire()
        self.selection(True,True)
        while pv > 0 and self.pv_physique > 0 :
            self.inventaire()
            self.mainWindow.printInTextArea("il est à ",distance," mètres de distance. Il a ",pv," pv")
            choix = ""
            while (choix != "avancer" and choix != "reculer" and choix != "rien"
                   and choix != "attaquer" and choix != "sort") :
                choix = self.mainWindow.waitForEntryText("Que fais-tu? ( avancer/ reculer/ attaquer/ rien)")
            if choix == "avancer" and distance > self.vitesse :
                distance -= self.vitesse
            elif choix == "avancer" and distance <= self.vitesse :
                distance = 1
            elif choix == "reculer" and nb_recul > 0 :
                nb_recul -= 1
                distance += self.vitesse
            elif choix == "reculer" and nb_recul < 0 :
                self.mainWindow.printInTextArea("Tu ne peux plus reculer")
            elif choix == "attaquer" and distance == 1 :
                self.selection(1,0)
                toucher = randrange(1, 20)
                if toucher <= sdes :
                    pv -= self.arme[0]
                    self.mainWindow.printInTextArea("Tu le frappes et lui inflige "),self.arme[0]," dégàts"
                else :
                    self.mainWindow.printInTextArea("Tu le rates")
            elif choix == "attaquer" and distance > 1 :
                self.mainWindow.printInTextArea("Impossible tu es trop loin de la cible")
                choix = ""
            else : ()

            if pv <= 0 :
                self.mainWindow.printInTextArea("Tu as vaincu!")
                self.PO += 100
                return True
            else :
                if distance > 1 and att < self.arme[0] and nb_recul_m > 0 :
                    self.mainWindow.printInTextArea("Il recule")
                    distance += vit
                    nb_recul_m -= 1
                elif (distance > 1 and att > self.arme[0]) or (distance > 1 and nb_recul_m == 0) :
                    self.mainWindow.printInTextArea("Il avance")
                    if vit > distance :
                        distance = 1
                    else :
                        distance -= vit
                elif distance == 1 :
                    toucher = randrange(1, 50)
                    if toucher <= sdes :
                        self.mainWindow.printInTextArea("Il t'attaque et t'inflige ",att," points de dégàts")
                        self.pv_physique -= att
                    else :
                        self.mainWindow.printInTextArea("Il n'arrive pas à te toucher")
        if self.pv_physique <= 0 :
            self.mainWindow.printInTextArea("VOUS ÊTES MORT")
            self.mainWindow.printInTextArea("FIN HERBE ROYALE")

            return False
        else :
            return True


    def jeu_taverne1(self): #jeu de chance dans la taverne 

        self.mainWindow.printInTextArea("les règles sont simples: devant vous se trouve un dé à 8 faces,")
        self.mainWindow.printInTextArea("Avant qu'il ne soit lancé, vous devez miser une somme de pièce d'or")
        self.mainWindow.printInTextArea("et ensuite parier soit sur un résultat paire ou impaire ce qui doublera")
        self.mainWindow.printInTextArea("votre mise soit sur un résultat précis ce qui quadruplera votre mise.")
        self.mainWindow.printInTextArea("Vous vous asseyez.")
        self.mainWindow.printInTextArea("Vous avez actuellement ",self.PO," pièces d'or")
        mise = 0
        mise = int(self.mainWindow.waitForEntryText("Combien voulez vous miser?"))
        self.mainWindow.printInTextArea("Vous avez misé ",mise," pièces d'or")
        choix = ""
        while (choix != "miser sur un chiffre paire ou impaire" and choix != "miser sur un chiffre précis"):
            choix = self.mainWindow.waitForEntryText("Comment misez vous? ( miser sur un chiffre paire ou impaire/ miser sur un chiffre précis)")
            choix = choix.lower()
        if choix == "miser sur un chiffre paire ou impaire":
            self.mainWindow.printInTextArea("Vous avez choisi de miser sur un chiffre paire ou impaire")
            choix2 = ""
            while (choix2 != "paire" and choix2 != "impaire"):
                choix2 = self.mainWindow.waitForEntryText("Sur quoi misez vous? ( paire/ impaire)")
                choix2 = choix2.lower()
            if choix2 == "paire":
                self.mainWindow.printInTextArea("Vous avez choisi un résultat paire, le dé est lancé...")
                dé = randrange(1, 8)
                if (dé == 2 or 4 or 6 or 8):
                    self.mainWindow.printInTextArea(dé,"Vous avez gagné")
                    self.PO = self.PO + (mise * 2)
                    self.mainWindow.printInTextArea("Vous avez donc maintenant: ",self.PO," pièces d'or")
                else:
                    self.mainWindow.printInTextArea(dé,"Vous avez perdu")
                    self.PO = self.PO - mise
                    self.mainWindow.printInTextArea("Vous avez donc maintenant: ",self.PO," pièces d'or")
            else:
                self.mainWindow.printInTextArea("Vous avez choisi un résultat impaire, le dé est lancé...")
                dé = randrange(1, 8)
                if (dé == 1 or 3 or 5 or 7):
                    self.mainWindow.printInTextArea(dé,"Vous avez gagné")
                    self.PO = self.PO + (mise * 2)
                    self.mainWindow.printInTextArea("Vous avez donc maintenant: ",self.PO," pièces d'or")
                else:
                    self.mainWindow.printInTextArea(dé,"Vous avez perdu")
                    self.PO = self.PO - mise
                    self.mainWindow.printInTextArea("Vous avez donc maintenant: ",self.PO," pièces d'or")
        elif choix == "miser sur un chiffre précis":
            self.mainWindow.printInTextArea("Vous avez choisi de miser sur un chiffre précis")
            choix2 = ""
            while (choix2 != 1 and choix2 != 2 and choix2 != 3 and choix2 != 4 and choix2 != 5 and choix2 != 6 and choix2 != 7 and choix2 != 8):
                choix2 = int(self.mainWindow.waitForEntryText("Quel chiffre choisissez-vous? ( un chffre en 1 et 8)"))
                self.mainWindow.printInTextArea("Vous avez choisi le chiffre: ",choix2,"le dé est lancé")
                dé = randrange(1, 8)
            if choix2 == dé:
                self.mainWindow.printInTextArea(dé,"Vous avez gagné")
                self.PO = self.PO + (mise * 4)
                self.mainWindow.printInTextArea("Vous avez donc maintenant: ",self.PO," pièces d'or")
            else:
                self.mainWindow.printInTextArea(dé,"Vous avez perdu")
                self.PO = self.PO - mise
                self.mainWindow.printInTextArea("Vous avez donc maintenant: ",self.PO," pièces d'or")
        self.pv_physique = 30
        self.inventaire()
        return True 

    def combat_final1(self): #combat final sans l'aide du sorcier
        self.mainWindow.printInTextArea("")
        self.mainWindow.printInTextArea("")
        nb_recul = 1
        nb_recul_m = 2
        distance = 7
        pv = 170
        vit = 3
        att = 20
        self.pv_physique += self.armure[0]
        self.mainWindow.printInTextArea ("Il vous attaque!")
        self.inventaire()
        self.selection(True,True,False)
        while pv > 0 and self.pv_physique > 0 :
            self.inventaire()
            self.mainWindow.printInTextArea("Le voleur est à ",distance," mètres de distance. Ils ont",pv," pv")
            choix = ""
            while (choix != "avancer" and choix != "reculer" and choix != "rien"
                   and choix != "attaquer" and choix != "sort") :
                choix = self.mainWindow.waitForEntryText("Que fais-tu? (avancer/ reculer/ attaquer/ rien )")
            if choix == "avancer" and distance > self.vitesse :
                distance -= self.vitesse
            elif choix == "avancer" and distance <= self.vitesse :
                distance = 1
            elif choix == "reculer" and nb_recul > 0 :
                nb_recul -= 1
                distance += self.vitesse
            elif choix == "reculer" and nb_recul < 0 :
                self.mainWindow.printInTextArea("Tu ne peux plus reculer")
            elif choix == "attaquer" and distance == 1 :
                self.selection(1,0,0)
                toucher = randrange(1, 20)
                if toucher <= sdes :
                    pv -= self.arme[0]
                    self.mainWindow.printInTextArea("Tu le frappes et lui inflige ",self.arme[0]," dégàts")
                else :
                    self.mainWindow.printInTextArea("Tu le rates")
            elif choix == "attaquer" and distance > 1 :
                self.mainWindow.printInTextArea("Impossible tu es trop loin de la cible")
                choix = ""
            # elif choix == "sort" :
            #     self.selection(False,False,True)
            #     if self.sort[2] <= distance :
            #         if self.sort[1] == "att" :
            #             pv -= self.sort[0]
            #             self.mainWindow.printInTextArea("Tu lances ce sort qui inflige",self.sort[0],"dégàts")
            #         else :
            #             choix = ""
            #     else :
            #         self.mainWindow.printInTextArea("Tu es trop près pour pouvoir lancer ton sort")
            #         choix = ""
            #     choix = ""
            else : ()
            if pv <= 0 :
                self.mainWindow.printInTextArea("Tu l'as tué!")
                return True
            else :
                if distance > 1 and att < self.arme[0] and nb_recul_m > 0 :
                    self.mainWindow.printInTextArea("Le voleur recule")
                    distance += vit
                    nb_recul_m -= 1
                elif (distance > 1 and att > self.arme[0]) or (distance > 1 and nb_recul_m == 0) :
                    self.mainWindow.printInTextArea("Le voleur avance")
                    if vit > distance :
                        distance = 1
                    else :
                        distance -= vit
                elif distance == 1 :
                    toucher = randrange(1, 20)
                    if toucher <= sdes :
                        self.mainWindow.printInTextArea("Il t'attaque et t'inflige ",att," points de dégàts")
                        self.pv_physique -= att
                    else :
                        self.mainWindow.printInTextArea("Il n'arrive pas à te toucher")
        if self.pv_physique <= 0 :
            self.mainWindow.printInTextArea("Il t'a tué!")
            return False
        else :
            return True


    def boutique_forgeron1(self): #achat arme et armure
        self.mainWindow.printInTextArea("Vous rentrez dans cette boutique où sont accrochés diverses armes")
        self.mainWindow.printInTextArea("et armures, un homme robuste arrive vers vous et vous demande")
        self.mainWindow.printInTextArea("se que vous souhaitez acheter vous regarder alors les prix sur")
        self.mainWindow.printInTextArea("les étagères: [épée 15 PO], [masse 20 PO], [Master_Sword 50 PO]")
        self.mainWindow.printInTextArea("Vous pensez à garder de l'argent pour acheter une armure:")
        self.mainWindow.printInTextArea("[armure de fer 30 PO], [armure d'acier 40 PO], [bouclier hylien 80 PO]")
        self.mainWindow.printInTextArea("le forgeron vous demande de choisir une arme premièrement.")
        self.mainWindow.printInTextArea("vous avez actuellement : ", self.PO ," pièces d'or.")
        choix = ""
        while (choix != "épée" and choix != "masse" and choix != "Master_Sword"and choix != "rien"): #choix arme
            choix = self.mainWindow.waitForEntryText("Qu'achetez-vous? ( épée/ masse/ Master_Sword/ rien")
            choix = choix.lower()
        if choix == "épée":
            if self.PO < 15:
                self.mainWindow.printInTextArea("vous n'avez pas assez d'argent")
                self.mainWindow.printInTextArea("vous sortez de la boutique")
            else:
                self.Armes.update({"épée":[10, 15, 1, 3]})
                self.PO -= 15
                self.mainWindow.printInTextArea("Vous avez acheté une épée il vous reste ", self.PO ," pièces d'or")
        elif choix == "masse":
            if self.PO < 20:
                self.mainWindow.printInTextArea("vous n'avez pas assez d'argent")
                self.mainWindow.printInTextArea("vous sortez de la boutique")
            else:
                self.Armes.update({"masse":[15, 20, 1, 5]})
                self.PO -= 20
                self.mainWindow.printInTextArea("Vous avez acheté une masse il vous reste ", self.PO ," pièces d'or")
        elif choix == "Master_Sword":
            if self.PO < 50:
                self.mainWindow.printInTextArea("vous n'avez pas assez d'argent")
                self.mainWindow.printInTextArea("vous sortez de la boutique")
            else:
                self.Armes.update({"Master_Sword":[35, 50, 1, 10]})
                self.PO -= 50
                self.mainWindow.printInTextArea("Vous avez acheté Mester_Sword il vous reste ", self.PO ," pièces d'or")
        elif choix == "rien":
            self.mainWindow.printInTextArea("Vous n'avez rien acheté il vous reste ", self.PO ," pièces d'or")
        self.mainWindow.printInTextArea("vous pouvez maintenant acheter une armure.")
        choix = ""
        while (choix != "armure de fer" and choix != "armure d'acier" and choix != "bouclier hylien" and choix != "rien"): #choix armure
            choix = self.mainWindow.waitForEntryText(" Qu'achetez-vous? ( armure de fer/ armure d'acier/ bouclier hylien/ rien")
            choix = choix.lower()
        if choix == "armure de fer":
            if self.PO < 30:
                self.mainWindow.printInTextArea("vous n'avez pas assez d'argent")
                self.mainWindow.printInTextArea("vous sortez de la boutique")
            else:
                self.Armures.update({"armure de fer":[3, 30, 1, 3]})
                self.PO -= 30
                self.mainWindow.printInTextArea("Vous avez acheté une arumre de fer il vous reste ", self.PO ," pièces d'or")
        elif choix == "armure d'acier":
            if self.PO < 40:
                self.mainWindow.printInTextArea("vous n'avez pas assez d'argent")
                self.mainWindow.printInTextArea("vous sortez de la boutique")
            else:
                self.Armures.update({"armure d'acier":[4, 40, 1, 5]})
                self.PO -= 40
                self.mainWindow.printInTextArea("Vous avez acheté une armure d'acier il vous reste ", self.PO ," pièces d'or")
        elif choix == "bouclier hylien":
            if self.PO < 80:
                self.mainWindow.printInTextArea("vous n'avez pas assez d'argent")
                self.mainWindow.printInTextArea("vous sortez de la boutique")
            else:
                self.Armures.update({"bouclier hylien":[20, 80, 1, 10]})
                self.PO -= 80
                self.mainWindow.printInTextArea("Vous avez acheté un bouclier hylien il vous reste ", self.PO ," pièces d'or")
        elif choix == "rien":
            self.mainWindow.printInTextArea("Vous n'avez rien acheté il vous reste ", self.PO ," pièces d'or")
        return True

    def frostmourne1(self): #recevoir l'arme FROSTMOURNE
        self.Armes.update({"FROSTMOURNE":[50, 0, 1, 20]})

    def illusion_mental(self):#-4 pv mentaux a cause du mauvais choix
        self.pv_mental -= 4

    def illusion_physique(self): #-6 pv physique à cause de l'illusion
        self.pv_physique -= 6
        self.inventaire

    def potion(self):# bonus de pv physique avec la potion
        self.pv_physique = 40
        self.inventaire()

    def tresor_basilic(self): # +100 pièce d'or quand basilic battu
        self.PO += 100


    def combat_final1(self): #combat final avec l'aide du sorcier
        self.mainWindow.printInTextArea("")
        self.mainWindow.printInTextArea("")
        nb_recul = 1
        nb_recul_m = 2
        distance = 7
        pv = 170
        vit = 3
        att = 20
        self.pv_physique += self.armure[0]
        self.mainWindow.printInTextArea ("Il vous attaque!")
        self.inventaire()
        self.selection(True,True,False)
        while pv > 0 and self.pv_physique > 0 :
            self.inventaire()
            self.mainWindow.printInTextArea("Le voleur est à ",distance," mètres de distance. Ils ont",pv," pv")
            choix = ""
            while (choix != "avancer" and choix != "reculer" and choix != "rien"
                   and choix != "attaquer" and choix != "sort") :
                choix = self.mainWindow.waitForEntryText("Que fais-tu? (avancer/ reculer/ attaquer/ rien )")
            if choix == "avancer" and distance > self.vitesse :
                distance -= self.vitesse
            elif choix == "avancer" and distance <= self.vitesse :
                distance = 1
            elif choix == "reculer" and nb_recul > 0 :
                nb_recul -= 1
                distance += self.vitesse
            elif choix == "reculer" and nb_recul < 0 :
                self.mainWindow.printInTextArea("Tu ne peux plus reculer")
            elif choix == "attaquer" and distance == 1 :
                self.selection(1,0,0)
                toucher = randrange(1, 20)
                if toucher <= sdes :
                    pv -= self.arme[0]
                    pv -= 20
                    self.mainWindow.printInTextArea("Tu le frappes et lui inflige ",self.arme[0]," dégàts")
                    self.mainWindow.printInTextArea("Le sorcier lui inflige en plus 20 de dégats")
                else :
                    self.mainWindow.printInTextArea("Tu le rates")
            elif choix == "attaquer" and distance > 1 :
                self.mainWindow.printInTextArea("Impossible tu es trop loin de la cible")
                choix = ""
            # elif choix == "sort" :
            #     self.selection(False,False,True)
            #     if self.sort[2] <= distance :
            #         if self.sort[1] == "att" :
            #             pv -= self.sort[0]
            #             self.mainWindow.printInTextArea("Tu lances ce sort qui inflige",self.sort[0],"dégàts")
            #         else :
            #             choix = ""
            #     else :
            #         self.mainWindow.printInTextArea("Tu es trop près pour pouvoir lancer ton sort")
            #         choix = ""
            #     choix = ""
            else : ()
            if pv <= 0 :
                self.mainWindow.printInTextArea("Tu l'as tué!")
                return True
            else :
                if distance > 1 and att < self.arme[0] and nb_recul_m > 0 :
                    self.mainWindow.printInTextArea("Le voleur recule")
                    distance += vit
                    nb_recul_m -= 1
                elif (distance > 1 and att > self.arme[0]) or (distance > 1 and nb_recul_m == 0) :
                    self.mainWindow.printInTextArea("Le voleur avance")
                    if vit > distance :
                        distance = 1
                    else :
                        distance -= vit
                elif distance == 1 :
                    toucher = randrange(1, 20)
                    if toucher <= sdes :
                        self.mainWindow.printInTextArea("Il t'attaque et t'inflige ",att," points de dégàts")
                        self.pv_physique -= att
                    else :
                        self.mainWindow.printInTextArea("Il n'arrive pas à te toucher")
        if self.pv_physique <= 0 :
            self.mainWindow.printInTextArea("Il t'a tué!")
            return False
        else :
            return True

