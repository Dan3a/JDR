    #classe_personnage_jdr

from random import randint, randrange

personnage = "chevalier"
sdes = 12

class Perso:

    def __init__(self):

        #global
        self.name = ""
        self.force = 1
        self.ruse = 1
        self.eloquence = 1
        self.attaque = 1
        self.armure = 1
        self.pouvoir = 1
        self.pv_physique = 20
        self.pv_mental = 10 
        self.etat = ""
        self.vitesse = 0
        self.PO = 1
        self.arme = []
        self.armure = []
        self.sort = []
        #Armes [degats, prix, nombre, force mini]
        self.Armes = {"dague":[2, 5, 1, 1], "épée":[4, 15, 0, 3], "masse":[5, 20, 0, 5], "fléau":[6, 25, 0, 5],
                        "Master_Sword":[12, 50, 0, 10], "Mjölnir":[15, 70, 0, 10], "FROSTMOURNE":[50, 0, 0, 20]}
        #Armures [protection, prix, nombre, force mini]
        self.Armures = {"gambison de cuir":[1, 10, 0, 1], "armure de fer":[3, 30, 0, 3], "armure d'acier":[4, 40, 0, 5],
                        "Armure_ancestral":[10, 60, 0, 7], "Bouclier_Hylien":[20, 80, 0, 10], "DAEDRIQUE":[60, 0, 0, 20]}

    #REPARTITION DES CARACTERISTIQUE DES PERSONNAGE AU DEBUT DE LA PARTIE
    def debut(self, mainWindow):
        self.mainWindow = mainWindow
        self.name = self.mainWindow.waitForEntryText("Quel est votre nom ? : ")
        self.pv_physique = 20
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
        if armure is True :
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
            elif (choix == list(self.Armures.keys())[0] and self.Armures["DAEDRIQUE"][2] > 0
                  and self.Armures["DAEDRIQUE"][3] <= self.cons) :
                self.armure = self.Armures["DAEDRIQUE"]
            elif (choix == list(self.Armures.keys())[3] and self.Armures["Bouclier_Hylien"][2] > 0
                  and self.Armures["Bouclier_Hylien"][3] <= self.cons) :
                self.armure = self.Armures["Bouclier_Hylien"]
            elif (choix == list(self.Armures.keys())[4] and self.Armures["Armure_ancestral"][2] > 0
                  and self.Armures["Armure_ancestral"][3] <= self.cons) :
                self.armure = self.Armures["Armure_ancestral"]
            elif (choix == list(self.Armures.keys())[5] and self.Armures["armure d'acier"][2] > 0
                  and self.Armures["armure d'acier"][3] <= self.cons) :
                self.armure = self.Armures["armure d'acier"]
            else :
                self.armure = [0]
            

        #choix des sorts
        # if sort is True :
        #     while (choix != "boule de feu mineur" and choix != "boule de feu majeur"
        #            and choix != "FLAMME" and choix != "TEMPUS"
        #            and choix != "DEPRETIO"
        #            and choix != "rien") :
        #         choix = self.mainWindow.waitForEntryText("Choix du sort : ")
        #         choix = choix.lower()
        #     if (choix == list(self.Sorts.keys())[0] and self.Sorts["boule de feu mineur"][2] > 0
        #         and self.Sorts["boule de feu mineur"][5] <= self.pouvoir) :
        #         self.sort = self.Sorts["boule de feu mineur"]
        #     elif (choix == list(self.Sorts.keys())[1] and self.Sorts["boule de feu majeur"][2] > 0
        #           and self.Sorts["boule de feu majeur"][5] <= self.pouvoir) :
        #         self.sort = self.Sorts["boule de feu majeur"]
        #     elif (choix == list(self.Sorts.keys())[2] and self.Sorts["FLAMME"][2] > 0
        #           and self.Sorts["FLAMME"][5] <= self.pouvoir) :
        #         self.sort = self.Sorts["FLAMME"]
        #     elif (choix == list(self.Sorts.keys())[3] and self.Sorts["TEMPUS"][2] > 0
        #           and self.Sorts["TEMPUS"][5] <= self.pouvoir) :
        #         self.sort = self.Sorts["TEMPUS"]
        #     elif (choix == list(self.Sorts.keys())[4] and self.Sorts["DEPRETIO"][2] > 0
        #           and self.Sorts["DEPRETIO"][5] <= self.pouvoir) :
        #         self.sort = self.Sorts["DEPRETIO"]
        #     else :
        #         self.sort = []

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
        self.mainWindow.printInTextArea("")
        self.mainWindow.printInTextArea (self.name,self.etat)

        self.mainWindow.printInTextArea("### Argent : ",self.argent," pièces d'or")

        self.mainWindow.printInTextArea("### Force  : ",self.force)

        self.mainWindow.printInTextArea("### Ruse   : ",self.ruse)

        self.mainWindow.printInTextArea("Inventaire :")

        for key,nb in self.Armes.items() :
            if nb[2] > 0 :
                self.mainWindow.printInTextArea ("- ",nb[2]," ",key)
        for key,nb in self.Armures.items() :
            if nb[2] > 0 :
                self.mainWindow.printInTextArea ("- ",nb[2]," ",key)
        # for key,nb in self.Sorts.items() :
        #     if nb[3] > 0 :
        #         self.mainWindow.printInTextArea ("-",nb[3],key)
        self.mainWindow.printInTextArea("")

    #DEFINITION DES DIFFERENTS MODULES DES COMBATS
    def fight(self, nom, att, ca, vit, dex, pv, distance) :
        
        nb_recul = 1
        nb_recul_m = 2
        self.mainWindow.printInTextArea ("Un",nom,"attaque")
        self.inventaire()
        self.selection(True,True,False)
        while pv > 0 and self.pv_physique > 0 :
            self.inventaire()
            self.mainWindow.printInTextArea("Le",nom,"est �",distance,"m�tres de distance. Il a ",pv," pv")
            choix = ""
            while (choix != "avancer" and choix != "reculer" and choix != "rien"
                   and choix != "attaque" and choix != "sort") :
                choix = self.mainWindow.waitForEntryText("Que fais-tu? ")
            if choix == "avancer" and distance > self.vitesse :
                distance -= self.vitesse
            elif choix == "avancer" and distance <= self.vitesse :
                distance = 1
            elif choix == "reculer" and nb_recul > 0 :
                nb_recul -= 1
                distance += self.vitesse
            elif choix == "reculer" and nb_recul < 0 :
                self.mainWindow.printInTextArea("Tu ne peux plus reculer")
            elif choix == "attaque" and distance == 1 :
                self.selection(1,0)
                toucher = randrange(1, 20)
                if toucher <= sdes :
                    pv -= self.arme[0]
                    self.mainWindow.printInTextArea("Tu le frappes et lui inflige"),self.arme[0],"dégàts"
                else :
                    self.mainWindow.printInTextArea("Tu le rates")
            elif choix == "attaque" and distance > 1 :
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
            #         self.mainWindow.printInTextArea("Tu es trop pr�s pour pouvoir lancer ton sort")
            #         choix = ""
            #     choix = ""
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
        if self.pva <= 0 :
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
        self.mainWindow.printInTextArea ("Les gardes vous attaquent")
        self.inventaire()
        self.selection(True,True)
        while pv > 0 and self.pv_physique > 0 :
            self.inventaire()
            self.mainWindow.printInTextArea("Les gardes sont à ",distance," mètres de distance. Ils ont",pv," pv")
            choix = ""
            while (choix != "avancer" and choix != "reculer" and choix != "rien"
                   and choix != "attaque" and choix != "sort") :
                choix = self.mainWindow.waitForEntryText("Que fais-tu? ")
            if choix == "avancer" and distance > self.vitesse :
                distance -= self.vitesse
            elif choix == "avancer" and distance <= self.vitesse :
                distance = 1
            elif choix == "reculer" and nb_recul > 0 :
                nb_recul -= 1
                distance += self.vitesse
            elif choix == "reculer" and nb_recul < 0 :
                self.mainWindow.printInTextArea("Tu ne peux plus reculer")
            elif choix == "attaque" and distance == 1 :
                self.selection(1,0)
                toucher = randrange(1, 20)
                if toucher <= sdes :
                    pv -= self.arme[0]
                    self.mainWindow.printInTextArea("Tu le frappes et lui inflige"),self.arme[0],"dégàts"
                else :
                    self.mainWindow.printInTextArea("Tu le rates")
            elif choix == "attaque" and distance > 1 :
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
                        self.mainWindow.printInTextArea("Ils t'attaquent et t'infligent",att,"points de dégàts")
                    else :
                        self.mainWindow.printInTextArea("Ils n'arrivent pas à te toucher")
        if self.pva <= 0 :
            self.mainWindow.printInTextArea("Ils t'ont tué!")
            return False
        else :
            return True

    
    def fight_dernier_guardien1(self) : #combat contre le dernier guardien à Icegate
        
        self.mainWindow.printInTextArea("")
        self.mainWindow.printInTextArea("Vous entez une présence très poche juste derrière vous,")
        self.mainWindow.printInTextArea("Vous distinguez à quelques mètres de vous un homme")
        self.mainWindow.printInTextArea("de votre taille lourdement habillé, il se trouve dans l'ombre")
        self.mainWindow.printInTextArea("et vous ne voyer pas son visage vous aller demander qui il est quand...")
        nb_recul = 1
        nb_recul_m = 2
        distance = 3
        pv = 25
        vit = 4
        att = 6
        self.mainWindow.printInTextArea ("Il vous attaque")
        self.inventaire()
        self.selection(True,True)
        while pv > 0 and self.pv_physique > 0 :
            self.inventaire()
            self.mainWindow.printInTextArea("il est à ",distance," mètres de distance. Il a ",pv," pv")
            choix = ""
            while (choix != "avancer" and choix != "reculer" and choix != "rien"
                   and choix != "attaque" and choix != "sort") :
                choix = self.mainWindow.waitForEntryText("Que fais-tu? ")
            if choix == "avancer" and distance > self.vitesse :
                distance -= self.vitesse
            elif choix == "avancer" and distance <= self.vitesse :
                distance = 1
            elif choix == "reculer" and nb_recul > 0 :
                nb_recul -= 1
                distance += self.vitesse
            elif choix == "reculer" and nb_recul < 0 :
                self.mainWindow.printInTextArea("Tu ne peux plus reculer")
            elif choix == "attaque" and distance == 1 :
                self.selection(1,0)
                toucher = randrange(1, 20)
                if toucher <= sdes :
                    pv -= self.arme[0]
                    self.mainWindow.printInTextArea("Tu le frappes et lui inflige"),self.arme[0],"dégàts"
                else :
                    self.mainWindow.printInTextArea("Tu le rates")
            elif choix == "attaque" and distance > 1 :
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
                    toucher = randrange(1, 20)
                    if toucher <= sdes :
                        self.mainWindow.printInTextArea("Il t'attaque et t'inflige ",att," points de dégàts")
                        self.pv_physique -= att

                    else :
                        self.mainWindow.printInTextArea("Il n'arrive pas à te toucher")
        if self.pva <= 0 :
            self.mainWindow.printInTextArea("Il t'as tué")
            return False
        else :
            return True


    def fight_souterrain1(self) : #combat dans souterrain contre basillic
        
        self.mainWindow.printInTextArea("")
        self.mainWindow.printInTextArea("Quand soudain, les murs de cette immense caverne se mettent à bouger")
        self.mainWindow.printInTextArea("comme un très grande spirale, jusqu'au moment où une tête faisant 5 fois")
        self.mainWindow.printInTextArea("votre taille descend vers vous, une tête au yeux mortelle et pleine d'écailles.")
        self.mainWindow.printInTextArea("Le Basillic, ce monstre ancestral que toutes les personnes ayant croisé son")
        self.mainWindow.printInTextArea("on fini pétrifié, vous restez figé, il s'immobilise jusqu'au moment où...")
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
                   and choix != "attaque" and choix != "sort") :
                choix = self.mainWindow.waitForEntryText("Que fais-tu? ")
            if choix == "avancer" and distance > self.vitesse :
                distance -= self.vitesse
            elif choix == "avancer" and distance <= self.vitesse :
                distance = 1
            elif choix == "reculer" and nb_recul > 0 :
                nb_recul -= 1
                distance += self.vitesse
            elif choix == "reculer" and nb_recul < 0 :
                self.mainWindow.printInTextArea("Tu ne peux plus reculer")
            elif choix == "attaque" and distance == 1 :
                self.selection(1,0)
                toucher = randrange(1, 20)
                if toucher <= sdes :
                    pv -= self.arme[0]
                    self.mainWindow.printInTextArea("Tu le frappes et lui inflige"),self.arme[0],"dégàts"
                else :
                    self.mainWindow.printInTextArea("Tu le rates")
            elif choix == "attaque" and distance > 1 :
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
                    toucher = randrange(1, 20)
                    if toucher <= sdes :
                        self.mainWindow.printInTextArea("Il t'attaque et t'inflige ",att," points de dégàts")
                        self.pv_physique -= att
                    else :
                        self.mainWindow.printInTextArea("Il n'arrive pas à te toucher")
        if self.pva <= 0 :
            self.mainWindow.printInTextArea("Il t'as tué")
            return False
        else :
            return True


    def jeu_taverne1(self, mise): #jeu de chance dans la taverne 

        self.mainWindow.printInTextArea("")
        self.mainWindow.printInTextArea("les régles sont simples: devant vous se trouve un dé à 8 faces,")
        self.mainWindow.printInTextArea("Avant qu'il soit lancé, vous devez misez une somme de pièce d'or")
        self.mainWindow.printInTextArea("et en suite parier soit sur un résultat paire ou impaire ce qui doublera")
        self.mainWindow.printInTextArea("votre mise soit sur un résultat précis ce qui quadruplera votre mise.")
        self.mainWindow.printInTextArea("Vous vous asseyez.")
        self.mainWindow.printInTextArea(", vous avez actuellement ",self.PO," pièces d'or")
        mise = 0
        mise = int(self.mainWindow.waitForEntryText("Combien voulez vous miser?"))
        int("Vous avez misez ",mise," pièces d'or")
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
                    self.mainWindow.printInTextArea(dé,"vous avez gagné")
                    self.PO = self.PO + (mise * 2)
                    self.mainWindow.printInTextArea("vous avez donc maintenant: ",self.PO," pièces d'or")
                else:
                    self.mainWindow.printInTextArea(dé,"Vous avez perdu")
                    self.PO = self.PO - mise
                    self.mainWindow.printInTextArea("vous avez donc maintenant: ",self.PO," pièces d'or")
            else:
                self.mainWindow.printInTextArea("Vous avez choisi un résultat impaire, le dé est lancé...")
                dé = randrange(1, 8)
                if (dé == 1 or 3 or 5 or 7):
                    self.mainWindow.printInTextArea(dé,"vous avez gagné")
                    self.PO = self.PO + (mise * 2)
                    self.mainWindow.printInTextArea("vous avez donc maintenant: ",self.PO," pièces d'or")
                else:
                    self.mainWindow.printInTextArea(dé,"Vous avez perdu")
                    self.PO = self.PO - mise
                    self.mainWindow.printInTextArea("vous avez donc maintenant: ",self.PO," pièces d'or")
        elif choix == "miser sur un chiffre précis":
            self.mainWindow.printInTextArea("vous avez choisi de miser sur un chiffre précis")
            choix2 = ""
            while (choix2 != 1 and choix2 != 2 and choix2 != 3 and choix2 != 4 and choix2 != 5 and choix2 != 6 and choix2 != 7 and choix2 != 8):
                choix2 = int(self.mainWindow.waitForEntryText("Quel chiffre choisissez-vous? ( un chffre en 1 et 8)"))
                self.mainWindow.printInTextArea("Vous avez choisit le chiffre: ",choix2,"le dé est lancé")
                dé = randrange(1, 8)
            if choix2 == dé:
                self.mainWindow.printInTextArea(dé,"vous avez gagné")
                self.PO = self.PO + (mise * 4)
                self.mainWindow.printInTextArea("vous avez donc maintenant: ",self.PO," pièces d'or")
            else:
                self.mainWindow.printInTextArea(dé,"vous avez perdu")
                self.PO = self.PO - mise
                self.mainWindow.printInTextArea("vous avez donc maintenant: ",self.PO," pièces d'or")
        return True 

    def combat_final1(self): #combat final sans l'aide du sorcier
        self.mainWindow.printInTextArea("")
        self.mainWindow.printInTextArea("")
        nb_recul = 1
        nb_recul_m = 2
        distance = 5
        pv = 100
        vit = 3
        att = 7
        self.mainWindow.printInTextArea ("Il vous attaque!")
        self.inventaire()
        self.selection(True,True,False)
        while pv > 0 and self.pv_physique > 0 :
            self.inventaire()
            self.mainWindow.printInTextArea("Le voleur est à ",distance," mètres de distance. Ils ont",pv," pv")
            choix = ""
            while (choix != "avancer" and choix != "reculer" and choix != "rien"
                   and choix != "attaque" and choix != "sort") :
                choix = self.mainWindow.waitForEntryText("Que fais-tu? ")
            if choix == "avancer" and distance > self.vitesse :
                distance -= self.vitesse
            elif choix == "avancer" and distance <= self.vitesse :
                distance = 1
            elif choix == "reculer" and nb_recul > 0 :
                nb_recul -= 1
                distance += self.vitesse
            elif choix == "reculer" and nb_recul < 0 :
                self.mainWindow.printInTextArea("Tu ne peux plus reculer")
            elif choix == "attaque" and distance == 1 :
                self.selection(1,0,0)
                toucher = randrange(1, 20)
                if toucher <= sdes :
                    pv -= self.arme[0]
                    self.mainWindow.printInTextArea("Tu le frappes et lui inflige",self.arme[0],"dégàts")
                else :
                    self.mainWindow.printInTextArea("Tu le rates")
            elif choix == "attaque" and distance > 1 :
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
                    self.mainWindow.printInTextArea("le voleur recule")
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
        if self.pva <= 0 :
            self.mainWindow.printInTextArea("Il t'as tué!")
            return False
        else :
            return True


    def boutique_forgeron1(self): #achat arme et armure
        self.mainWindow.printInTextArea("")
        self.mainWindow.printInTextArea("Vous rentrez dans cette boutique où sont accrochés diverses armes")
        self.mainWindow.printInTextArea("et armures, un homme robuste arrive vers vous et vous demande")
        self.mainWindow.printInTextArea("se que vous souhaitez acheter vous regarder alors les prix sur")
        self.mainWindow.printInTextArea("les étagères: [épée 15 PO], [masse 20 PO], [Master_Sword 50 PO]")
        self.mainWindow.printInTextArea("Vous pensez à garder de l'argent pour acheter une armure:")
        self.mainWindow.printInTextArea("[armure de fer 30 PO], [armure d'acier 40 PO], [Bouclier_Hylien 80 PO]")
        self.mainWindow.printInTextArea("le forgeron vous demande de choisir une arme premièrement.")
        self.mainWindow.printInTextArea("vous avez actuellement :", self.PO ,"pièces d'or.")
        choix = ""
        while (choix != "épée" and choix != "masse" and choix != "Master_Sword"and choix != "rien"): #choix arme
            choix = self.mainWindow.waitForEntryText("Qu'achetez-vous? ( épée/ masse/ Master_Sword/ rien")
            choix = choix.lower()
        if choix == "épée":
            if self.PO < 15:
                self.mainWindow.printInTextArea("")
                self.mainWindow.printInTextArea("vous n'avez pas assez d'argent")
                self.mainWindow.printInTextArea("vous sortez de la boutique")
            else:
                self.arme = "épée"
                self.PO -= 15
                self.mainWindow.printInTextArea("")
                self.mainWindow.printInTextArea("Vous avez acheté une épée il vous reste", self.PO ,"pièces d'or")
        elif choix == "masse":
            if self.PO < 20:
                self.mainWindow.printInTextArea("")
                self.mainWindow.printInTextArea("vous n'avez pas assez d'argent")
                self.mainWindow.printInTextArea("vous sortez de la boutique")
            else:
                self.arme = "masse"
                self.PO -= 20
                self.mainWindow.printInTextArea("")
                self.mainWindow.printInTextArea("Vous avez acheté une masse il vous reste", self.PO ,"pièces d'or")
        elif choix == "Master_Sword":
            if self.PO < 50:
                self.mainWindow.printInTextArea("")
                self.mainWindow.printInTextArea("vous n'avez pas assez d'argent")
                self.mainWindow.printInTextArea("vous sortez de la boutique")
            else:
                self.arme = "masse"
                self.PO -= 50
                self.mainWindow.printInTextArea("")
                self.mainWindow.printInTextArea("Vous avez acheté Mester_Sword il vous reste", self.PO ,"pièces d'or")
        elif choix == "rien":
            self.mainWindow.printInTextArea("")
            self.mainWindow.printInTextArea("Vous n'avez rien acheté il vous reste", self.PO ,"pièces d'or")
        self.mainWindow.printInTextArea("")
        self.mainWindow.printInTextArea("vous pouvez maintenant acheter une armure.")
        choix = ""
        while (choix != "armure de fer" and choix != "armure d'acier" and choix != "Bouclier_Hylien" and choix != "rien"): #choix armure
            choix = self.mainWindow.waitForEntryText(" Qu'achetez-vous? ( armure de fer/ armure d'acier/ Bouclier_Hylien/ rien")
            choix = choix.lower()
        if choix == "armure de fer":
            if self.PO < 30:
                self.mainWindow.printInTextArea("")
                self.mainWindow.printInTextArea("vous n'avez pas assez d'argent")
                self.mainWindow.printInTextArea("vous sortez de la boutique")
            else:
                self.arme = "armure de fer"
                self.PO -= 30
                self.mainWindow.printInTextArea("")
                self.mainWindow.printInTextArea("Vous avez acheté une arumre de fer il vous reste", self.PO ,"pièces d'or")
        elif choix == "armure d'acier":
            if self.PO < 40:
                self.mainWindow.printInTextArea("")
                self.mainWindow.printInTextArea("vous n'avez pas assez d'argent")
                self.mainWindow.printInTextArea("vous sortez de la boutique")
            else:
                self.arme = "armure d'acier"
                self.PO -= 40
                self.mainWindow.printInTextArea("")
                self.mainWindow.printInTextArea("Vous avez acheté une armure d'acier il vous reste", self.PO ,"pièces d'or")
        elif choix == "Bouclier_Hylien":
            if self.PO < 80:
                self.mainWindow.printInTextArea("")
                self.mainWindow.printInTextArea("vous n'avez pas assez d'argent")
                self.mainWindow.printInTextArea("vous sortez de la boutique")
            else:
                self.arme = "Bouclier_Hylien"
                self.PO -= 80
                self.mainWindow.printInTextArea("")
                self.mainWindow.printInTextArea("Vous avez acheté un Bouclier_Hylien il vous reste", self.PO ,"pièces d'or")
        elif choix == "rien":
            self.mainWindow.printInTextArea("")
            self.mainWindow.printInTextArea("Vous n'avez rien acheté il vous reste", self.PO ,"pièces d'or")
        return True