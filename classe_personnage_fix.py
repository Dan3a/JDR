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

from pygame import mixer

import os

personnage = "chevalier"
sdes = 12

class Perso:

    mixer.init()


    def playGardienSong(self):
        mixer.music.stop()
        mixer.music.load("assets/songs/gardien.mp3")
        mixer.music.play(loops=999)
    
    def playGardiensDebutSong(self):
        mixer.music.stop()
        mixer.music.load("assets/songs/combat_garde.mp3")
        mixer.music.play(loops=999)

    def playTaverneBoutiqueSong(self):
        mixer.music.stop()
        mixer.music.load("assets/songs/taverne+boutique.mp3")
        mixer.music.play(loops=999)
    
    def playCombatFinalSong(self):
        mixer.music.stop()
        mixer.music.load("assets/songs/combat_final.mp3")
        mixer.music.play(loops=999)
    
    def playBasiliqueSong(self):
        mixer.music.stop()
        mixer.music.load("assets/songs/basilique.mp3")
        mixer.music.play(loops=999)
    
    def playMortSong(self):
        mixer.music.stop()
        mixer.music.load("assets/songs/mort.mp3")
        mixer.music.play(loops=0)

    def playBackgroundSong(self):
        mixer.music.stop()
        mixer.music.load("assets/songs/background.mp3")
        mixer.music.play(loops=999)

    def stopMusic(self):
        mixer.music.stop()

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
        self.Armes = {
            "dague":[4, 5, 1, 1], 
            "??p??e":[10, 15, 0, 3], 
            "masse":[15, 20, 0, 5], 
            "fl??au":[18, 25, 0, 5],
            "master sword":[35, 50, 0, 10], 
            "mj??lnir":[42, 70, 0, 10], 
            "frostmourne":[50, 0, 0, 20]}

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
        self.playBackgroundSong()
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
        if arme:
            choisi = False
            while choisi == False:
                while (choix in self.Armes) == False:
                    choix = self.mainWindow.waitForEntryText("Choix d'arme : ")
                    choix = choix.lower()
                
                if (self.Armes[choix][2] > 0 and self.Armes[choix][3] <= self.force):
                    self.arme = self.Armes[choix]
                    choisi = True

                elif (self.Armes[choix][2] > 0) == False:
                    self.mainWindow.printInTextArea("Vous ne possedez pas cette arme.")

                else:
                    self.mainWindow.printInTextArea("Vous n'avez pas assez de force pour utiliser cette arme.")



        #choix des armures
        if armure is True :
            # choix = ""
            while (choix != list(self.Armures.keys())[0] and choix != list(self.Armures.keys())[1]
                   and choix != list(self.Armures.keys())[2] and choix != list(self.Armures.keys())[3]
                   and choix != list(self.Armures.keys())[4] and choix != list(self.Armures.keys())[5]
                   and choix != "rien") :
                choix = self.mainWindow.waitForEntryText("Choix d'armure : (tapez 'rien' si vide)")
                choix = choix.lower()
            if (choix == list(self.Armures.keys())[1] and self.Armures["gambison de cuir"][2] > 0
                and self.Armures["gambison de cuir"][3] <= self.cons) :
                self.armure = self.Armures["gambison de cuir"]
            elif (choix == list(self.Armures.keys())[2] and self.Armures["armure de fer"][2] > 0
                  and self.Armures["armure de fer"][3] <= self.cons) :
                self.armure = self.Armures["armure de fer"]
            elif (choix == list(self.Armures.keys())[0] and self.Armures["daedrique"][2] > 0
                  and self.Armures["daedrique"][3] <= self.cons) :
                self.armure = self.Armures["daedrique"]
            elif (choix == list(self.Armures.keys())[3] and self.Armures["bouclier hylien"][2] > 0
                  and self.Armures["bouclier hylien"][3] <= self.cons) :
                self.armure = self.Armures["bouclier hylien"]
            elif (choix == list(self.Armures.keys())[4] and self.Armures["armure ancestrale"][2] > 0
                  and self.Armures["armure ancestrale"][3] <= self.cons) :
                self.armure = self.Armures["armure ancestrale"]
            elif (choix == list(self.Armures.keys())[5] and self.Armures["armure d'acier"][2] > 0
                  and self.Armures["armure d'acier"][3] <= self.cons) :
                self.armure = self.Armures["armure d'acier"]
            else :
                self.armure = [0]
            
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
            self.etat = " est bless?? et a besoin de soins"
        else :
            self.etat = " est gravement bless??"
        self.mainWindow.printInTextArea (self.name,self.etat)

        self.mainWindow.printInTextArea("### Argent : ",self.PO," pi??ces d'or")

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
            self.mainWindow.printInTextArea("Le",nom,"est ?? ",distance," m??tres de distance. Il a ",pv," pv")
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
                toucher = randrange(1, 20)
                if toucher <= sdes :
                    pv -= self.arme[0]
                    self.mainWindow.printInTextArea("Tu le frappes et lui inflige" ),self.arme[0]," d??g??ts"
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
                        self.mainWindow.printInTextArea("Il t'attaque et t'inflige ",att," points de d??g??ts")
                        self.pv_physique -= att
                    else :
                        self.mainWindow.printInTextArea("Il n'arrive pas ?? te toucher")
        if self.pv_physique <= 0 :
            self.mainWindow.printInTextArea("Il t'a tu??!")
            return False
        else :
            return True

    
    def fight_Refus(self) : #combat du d??but contre les guardes (forc??ment perdu)
        
        nb_recul = 1
        nb_recul_m = 2
        distance = 5
        pv = 100
        vit = 3
        att = 20
        self.playGardiensDebutSong()
        self.inventaire()
        self.selection(True,True)
        self.mainWindow.printInTextArea ("Les gardes vous attaquent")
        while pv > 0 and self.pv_physique > 0 :
            self.inventaire()
            self.mainWindow.printInTextArea("Les gardes sont ?? ",distance," m??tres de distance. Ils ont ",pv," pv")
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
                    self.mainWindow.printInTextArea("Tu le frappes et lui inflige ",self.arme[0]," d??g??ts")
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
                        self.mainWindow.printInTextArea("Ils t'attaquent et t'infligent ",att," points de d??g??ts")
                        self.pv_physique -= att
                    else :
                        self.mainWindow.printInTextArea("Ils n'arrivent pas ?? te toucher")
        if self.pv_physique <= 0 :
            self.mainWindow.printInTextArea("VOUS ??TES MORT")
            self.mainWindow.printInTextArea("FIN FUYARDE")
            # self.deletionProcess()
            self.playMortSong()
            raise SystemExit(0) 
        else :
            return True

    
    def fight_dernier_gardien(self) : #combat contre le dernier guardien ?? Icegate
    
        self.mainWindow.printInTextArea("Vous entez une pr??sence tr??s poche juste derri??re vous,")
        self.mainWindow.printInTextArea("Vous distinguez ?? quelques m??tres de vous un homme")
        self.mainWindow.printInTextArea("de votre taille lourdement habill??, il se trouve dans l'ombre")
        self.mainWindow.printInTextArea("et vous ne voyer pas son visage vous aller demander qui il est quand...")
        nb_recul = 1
        nb_recul_m = 2
        distance = 3
        pv = 24
        vit = 4
        att = 6
        self.playGardienSong()
        self.mainWindow.printInTextArea ("Il vous attaque")
        self.inventaire()
        self.selection(True,True)
        while pv > 0 and self.pv_physique > 0 :
            self.inventaire()
            self.mainWindow.printInTextArea("il est ?? ",distance," m??tres de distance. Il a ",pv," pv")
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
                toucher = randrange(1, 20)
                if toucher <= sdes :
                    pv -= self.arme[0]
                    self.mainWindow.printInTextArea("Tu le frappes et lui inflige ",self.arme[0]," d??g??ts")
                else :
                    self.mainWindow.printInTextArea("Tu le rates")
            elif choix == "attaque" and distance > 1 :
                self.mainWindow.printInTextArea("Impossible tu es trop loin de la cible")
                choix = ""
            else : ()


            if pv <= 0 :
                self.mainWindow.printInTextArea("Tu as vaincu!")
                self.force = 20
                self.Armes["frostmourne"] = [50, 0, 1, 20]
                self.playBackgroundSong()
                
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
                        self.mainWindow.printInTextArea("Il t'attaque et t'inflige ",att," points de d??g??ts")
                        self.pv_physique -= att

                    else :
                        self.mainWindow.printInTextArea("Il n'arrive pas ?? te toucher")
        if self.pv_physique <= 0 :
            self.mainWindow.printInTextArea("Il t'as tu??")
            self.playMortSong()
            return False
        else :
            return True

    def fight_souterrain1(self) : #combat dans souterrain contre basillic
    
        self.mainWindow.printInTextArea("Quand soudain, les murs de cette immense caverne se mettent ?? bouger")
        self.mainWindow.printInTextArea("comme une tr??s grande spirale, jusqu'au moment o?? une t??te faisant 5 fois")
        self.mainWindow.printInTextArea("votre taille descend vers vous, une t??te au yeux mortels et pleine d'??cailles.")
        self.mainWindow.printInTextArea("Le Basillic, ce monstre mythique que toutes les personnes ayant crois??")
        self.mainWindow.printInTextArea("ont finis p??trifi??s. Vous restez fig??, il s'immobilise jusqu'au moment o??...")
        nb_recul = 1
        nb_recul_m = 2
        distance = 9
        pv = 200
        vit = 4
        att = 14
        self.playGardienSong()
        self.mainWindow.printInTextArea ("Il vous attaque")
        self.inventaire()
        self.selection(True,True)
        while pv > 0 and self.pv_physique > 0 :
            self.inventaire()
            self.mainWindow.printInTextArea("il est ?? ",distance," m??tres de distance. Il a ",pv," pv")
            choix = ""
            while (choix != "avancer" and choix != "reculer" and choix != "rien"
                    and choix != "attaquer" and choix != "sort") :
                choix = self.mainWindow.waitForEntryText("Que fais-tu? (avancer/ reculer/ attaquer/ rien )")
            if choix == "avancer" and distance > self.vitesse :
                distance -= self.vitesse
            elif   choix == "avancer" and distance <= self.vitesse :
                distance = 1
            elif choix == "reculer" and nb_recul > 0 :
                nb_recul -= 1
                distance += self.vitesse
            elif choix == "reculer" and nb_recul < 0 :
                self.mainWindow.printInTextArea("Tu ne peux plus reculer")
            elif choix == "attaquer" and distance == 1 :
                toucher = randrange(1, 20)
                if toucher <= sdes :
                    pv -= self.arme[0]
                    self.mainWindow.printInTextArea("Tu le frappes et lui inflige ",self.arme[0]," d??g??ts")
                else :
                    self.mainWindow.printInTextArea("Tu le rates")
            elif choix == "attaque" and distance > 1 :
                self.mainWindow.printInTextArea("Impossible tu es trop loin de la cible")
                choix = ""
            else : ()


            if pv <= 0 :
                self.mainWindow.printInTextArea("Tu as vaincu!")
                self.force = 20
                self.Armes["frostmourne"] = [50, 0, 1, 20]
                self.playBackgroundSong()
                
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
                    toucher = randrange(1, 32)
                    if toucher <= sdes :
                        self.mainWindow.printInTextArea("Il t'attaque et t'inflige ",att," points de d??g??ts")
                        self.pv_physique -= att

                    else :
                        self.mainWindow.printInTextArea("Il n'arrive pas ?? te toucher")
        if self.pv_physique <= 0 :
            self.mainWindow.printInTextArea("Il t'as tu??")
            self.playMortSong()
            return False
        else :
            return True



    def jeu_taverne1(self): #jeu de chance dans la taverne 
        self.playTaverneBoutiqueSong()
        self.mainWindow.printInTextArea("les r??gles sont simples: devant vous se trouve un d?? ?? 8 faces,")
        self.mainWindow.printInTextArea("Avant qu'il ne soit lanc??, vous devez miser une somme de pi??ce d'or")
        self.mainWindow.printInTextArea("et ensuite parier soit sur un r??sultat paire ou impaire ce qui doublera")
        self.mainWindow.printInTextArea("votre mise soit sur un r??sultat pr??cis ce qui quadruplera votre mise.")
        self.mainWindow.printInTextArea("Vous vous asseyez.")
        self.mainWindow.printInTextArea("Vous avez actuellement ",self.PO," pi??ces d'or")
        mise = 0
        mise = int(self.mainWindow.waitForEntryText("Combien voulez vous miser?"))
        self.mainWindow.printInTextArea("Vous avez mis?? ",mise," pi??ces d'or")
        choix = ""
        while (choix != "miser sur un chiffre paire ou impaire" and choix != "miser sur un chiffre pr??cis"):
            choix = self.mainWindow.waitForEntryText("Comment misez vous? ( miser sur un chiffre paire ou impaire/ miser sur un chiffre pr??cis)")
            choix = choix.lower()
        if choix == "miser sur un chiffre paire ou impaire":
            self.mainWindow.printInTextArea("Vous avez choisi de miser sur un chiffre paire ou impaire")
            choix2 = ""
            while (choix2 != "paire" and choix2 != "impaire"):
                choix2 = self.mainWindow.waitForEntryText("Sur quoi misez vous? ( paire/ impaire)")
                choix2 = choix2.lower()
            if choix2 == "paire":
                self.mainWindow.printInTextArea("Vous avez choisi un r??sultat paire, le d?? est lanc??...")
                d?? = randrange(1, 8)
                if (d?? % 2 == 0):
                    self.mainWindow.printInTextArea(d??,", vous avez gagn??")
                    self.PO = self.PO + (mise * 2)
                    self.mainWindow.printInTextArea("Vous avez donc maintenant: ",self.PO," pi??ces d'or")
                else:
                    self.mainWindow.printInTextArea(d??,", vous avez perdu")
                    self.PO = self.PO - mise
                    self.mainWindow.printInTextArea("Vous avez donc maintenant: ",self.PO," pi??ces d'or")
            else:
                self.mainWindow.printInTextArea("Vous avez choisi un r??sultat impaire, le d?? est lanc??...")
                d?? = randrange(1, 8)
                if (d?? % 2 != 0):
                    self.mainWindow.printInTextArea(d??,", vous avez gagn??")
                    self.PO = self.PO + (mise * 2)
                    self.mainWindow.printInTextArea("Vous avez donc maintenant: ",self.PO," pi??ces d'or")
                else:
                    self.mainWindow.printInTextArea(d??,", vous avez perdu")
                    self.PO = self.PO - mise
                    self.mainWindow.printInTextArea("Vous avez donc maintenant: ",self.PO," pi??ces d'or")
        elif choix == "miser sur un chiffre pr??cis":
            self.mainWindow.printInTextArea("Vous avez choisi de miser sur un chiffre pr??cis")
            choix2 = ""
            while (choix2 != 1 and choix2 != 2 and choix2 != 3 and choix2 != 4 and choix2 != 5 and choix2 != 6 and choix2 != 7 and choix2 != 8):
                choix2 = int(self.mainWindow.waitForEntryText("Quel chiffre choisissez-vous? ( un chffre en 1 et 8)"))
                self.mainWindow.printInTextArea("Vous avez choisi le chiffre: ",choix2,"le d?? est lanc??")
                d?? = randrange(1, 8)
            if choix2 == d??:
                self.mainWindow.printInTextArea(d??,"Vous avez gagn??")
                self.PO = self.PO + (mise * 4)
                self.mainWindow.printInTextArea("Vous avez donc maintenant: ",self.PO," pi??ces d'or")
                self.playBackgroundSong()
            else:
                self.mainWindow.printInTextArea(d??," Vous avez perdu")
                self.PO = self.PO - mise
                self.mainWindow.printInTextArea("Vous avez donc maintenant: ",self.PO," pi??ces d'or")
                self.playBackgroundSong()
        self.pv_physique = 30
        self.inventaire()
        return True 

    def combat_final1(self): #combat final sans l'aide du sorcier
        self.playCombatFinalSong()
        nb_recul = 1
        nb_recul_m = 2
        distance = 5
        pv = 100
        vit = 3
        att = 7
        self.mainWindow.printInTextArea ("Il vous attaque!")
        self.inventaire()
        self.selection(True,True)
        while pv > 0 and self.pv_physique > 0 :
            self.inventaire()
            self.mainWindow.printInTextArea("Le voleur est ?? ",distance," m??tres de distance. Ils ont",pv," pv")
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
                toucher = randrange(1, 20)
                if toucher <= sdes :
                    pv -= self.arme[0]
                    self.mainWindow.printInTextArea("Tu le frappes et lui inflige ",self.arme[0]," d??g??ts")
                else :
                    self.mainWindow.printInTextArea("Tu le rates")

            elif choix == "attaquer" and distance > 1 :
                self.mainWindow.printInTextArea("Impossible tu es trop loin de la cible")
                choix = ""
            else : ()
            if pv <= 0 :
                self.mainWindow.printInTextArea("Tu l'as tu??!")
                self.playBackgroundSong()
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
                        self.mainWindow.printInTextArea("Il t'attaque et t'inflige ",att," points de d??g??ts")
                        self.pv_physique -= att
                    else :
                        self.mainWindow.printInTextArea("Il n'arrive pas ?? te toucher")
        if self.pv_physique <= 0 :
            self.mainWindow.printInTextArea("Il t'a tu??!")
            self.playMortSong()
            return False
        else :
            return True


    def boutique_forgeron1(self): #achat arme et armure
        self.playTaverneBoutiqueSong()
        self.mainWindow.printInTextArea("Vous rentrez dans cette boutique o?? sont accroch??s diverses armes")
        self.mainWindow.printInTextArea("et armures, un homme robuste arrive vers vous et vous demande")
        self.mainWindow.printInTextArea("se que vous souhaitez acheter vous regarder alors les prix sur")
        self.mainWindow.printInTextArea("les ??tag??res: [??p??e 15 PO], [masse 20 PO], [master word 50 PO]")
        self.mainWindow.printInTextArea("Vous pensez ?? garder de l'argent pour acheter une armure:")
        self.mainWindow.printInTextArea("[armure de fer 30 PO], [armure d'acier 40 PO], [bouclier hylien 80 PO]")
        self.mainWindow.printInTextArea("le forgeron vous demande de choisir une arme premi??rement.")
        self.mainWindow.printInTextArea("vous avez actuellement : ", self.PO ," pi??ces d'or.")


        choix = ""
        while (choix != "??p??e" and choix != "masse" and choix != "master sword"and choix != "rien"): #choix arme
            choix = self.mainWindow.waitForEntryText("Qu'achetez-vous? ( ??p??e/ masse/ master sword/ rien")
            choix = choix.lower()
        if choix == "??p??e":
            if self.PO < 15:
                self.mainWindow.printInTextArea("Vous n'avez pas assez d'argent")
                self.mainWindow.printInTextArea("Vous sortez de la boutique")
            else:
                self.Armes.update({"??p??e":[10, 15, 1, 3]})
                self.PO -= 15
                self.mainWindow.printInTextArea("Vous avez achet?? une ??p??e il vous reste ", self.PO ," pi??ces d'or")
        elif choix == "masse":
            if self.PO < 20:
                self.mainWindow.printInTextArea("Vous n'avez pas assez d'argent")
                self.mainWindow.printInTextArea("Vous sortez de la boutique")
            else:
                self.Armes.update({"masse":[15, 20, 1, 5]})
                self.PO -= 20
                self.mainWindow.printInTextArea("Vous avez achet?? une masse il vous reste ", self.PO ," pi??ces d'or")
        elif choix == "master sword":
            if self.PO < 50:
                self.mainWindow.printInTextArea("Vous n'avez pas assez d'argent")
                self.mainWindow.printInTextArea("Vous sortez de la boutique")
            else:
                self.Armes.update({"master sword":[35, 50, 1, 10]})
                self.PO -= 50
                self.mainWindow.printInTextArea("Vous avez achet?? Mester_Sword il vous reste ", self.PO ," pi??ces d'or")
        elif choix == "rien":
            self.mainWindow.printInTextArea("Vous n'avez rien achet?? il vous reste ", self.PO ," pi??ces d'or")
        self.mainWindow.printInTextArea("vous pouvez maintenant acheter une armure.")
        choix = ""
        while (choix != "armure de fer" and choix != "armure d'acier" and choix != "bouclier hylien" and choix != "rien"): #choix armure
            choix = self.mainWindow.waitForEntryText(" Qu'achetez-vous? ( armure de fer/ armure d'acier/ bouclier hylien/ rien")
            choix = choix.lower()
        if choix == "armure de fer":
            if self.PO < 30:
                self.mainWindow.printInTextArea("Vous n'avez pas assez d'argent")
                self.mainWindow.printInTextArea("Vous sortez de la boutique")
            else:
                self.Armures.update({"armure de fer":[3, 30, 1, 3]})
                self.PO -= 30
                self.mainWindow.printInTextArea("Vous avez achet?? une arumre de fer il vous reste ", self.PO ," pi??ces d'or")
        elif choix == "armure d'acier":
            if self.PO < 40:
                self.mainWindow.printInTextArea("Vous n'avez pas assez d'argent")
                self.mainWindow.printInTextArea("Vous sortez de la boutique")
            else:
                self.Armures.update({"armure d'acier":[4, 40, 1, 5]})
                self.PO -= 40
                self.mainWindow.printInTextArea("Vous avez achet?? une armure d'acier il vous reste ", self.PO ," pi??ces d'or")
        elif choix == "bouclier hylien":
            if self.PO < 80:
                self.mainWindow.printInTextArea("Vous n'avez pas assez d'argent")
                self.mainWindow.printInTextArea("Vous sortez de la boutique")
            else:
                self.Armures.update({"bouclier hylien":[20, 80, 1, 10]})
                self.PO -= 80
                self.mainWindow.printInTextArea("Vous avez achet?? un bouclier hylien il vous reste ", self.PO ," pi??ces d'or")
        elif choix == "rien":
            self.mainWindow.printInTextArea("Vous n'avez rien achet?? il vous reste ", self.PO ," pi??ces d'or")
        self.playBackgroundSong()
        return True

    def illusion_mental(self):#-4 pv mentaux a cause du mauvais choix
        self.pv_mental -= 4

    def illusion_physique(self): #-6 pv physique ?? cause de l'illusion
        self.pv_physique -= 6
        self.inventaire

    def potion(self):# bonus de pv physique avec la potion
        self.pv_physique = 40
        self.mainWindow.printInTextArea("")
        self.inventaire()

    def tresor_basilic(self): # +100 pi??ce d'or quand basilic battu
        self.PO += 100


    def combat_final2(self): #combat final avec l'aide du sorcier
        self.playCombatFinalSong()
        nb_recul = 1
        nb_recul_m = 2
        distance = 7
        pv = 170
        vit = 3
        att = 20
        self.pv_physique += self.armure[0]
        self.mainWindow.printInTextArea ("Il vous attaque!")
        self.inventaire()
        self.selection(True,True)
        while pv > 0 and self.pv_physique > 0 :
            self.inventaire()
            self.mainWindow.printInTextArea("Le voleur est ?? ",distance," m??tres de distance. Il a ",pv," pv")
            choix = ""
            while (choix != "avancer" and choix != "reculer" and choix != "rien"
                   and choix != "attaquer" and choix != "sort") :
                choix = self.mainWindow.waitForEntryText("Que fais-tu? (avancer/ reculer/ attaquer/ rien )")
                print(self.armure[0])
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
                toucher = randrange(1, 20)
                if toucher <= sdes :
                    pv -= self.arme[0]
                    pv -= 20
                    self.mainWindow.printInTextArea("Tu le frappes et lui inflige ",self.arme[0]," d??g??ts")
                    self.mainWindow.printInTextArea("Le sorcier lui inflige en plus 20 de d??gats")
                else :
                    self.mainWindow.printInTextArea("Tu le rates")

            elif choix == "attaquer" and distance > 1 :
                self.mainWindow.printInTextArea("Impossible tu es trop loin de la cible")
                choix = ""
            else : ()
            if pv <= 0 :
                self.mainWindow.printInTextArea("Tu l'as tu??!")
                self.playMortSong()
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
                        self.mainWindow.printInTextArea("Il t'attaque et t'inflige ",att," points de d??g??ts")
                        self.pv_physique -= att
                    else :
                        self.mainWindow.printInTextArea("Il n'arrive pas ?? te toucher")
        if self.pv_physique <= 0 :
            self.mainWindow.printInTextArea("Il t'a tu??!")
            self.playMortSong()
            return False
        else :
            self.playBackgroundSong()
            return True

