#classe_personnage_jdr

from random import randrange

personnage = "voleur"
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
        self.argent = 1
        self.arme = []
        self.armure = []
        self.sort = []
        #Armes [degats, prix, nombre, force mini]
        self.Armes = {"dague ":[2, 5, 1, 1], "épée":[4, 15, 0, 3], "masse":[5, 20, 0, 5], "fléau":[6, 25, 0, 5],
                        "Master_Sword":[12, 50, 0, 10], "Mjölnir":[15, 70, 0, 10], "FROSTMOURNE":[50, 0, 0, 20]}
        #Armures [protection, prix, nombre, force mini]
        self.Armures = {"gambison de cuir":[1, 10, 0, 1], "armure de fer":[3, 30, 0, 3], "armure d'acier":[4, 40, 0, 5],
                        "Armure_ancestral":[10, 60, 0, 7], "Bouclier_Hylien":[20, 80, 0, 10], "DAEDRIQUE":[60, 0, 0, 20]}
        #Sort [degat, type(defaut/crystaux), distance min, pouvoir mini]
        self.Sorts = {"boule de feu mineur":[3, 1, 2, 2], "boule de feu majeur":[5, 1, 3, 3], "FLAMME":[+10, 2, 1, 8],
                        "TEMPUS":[0, 2, 1, 8], "DEPRETIO":[100, 2, 5, 20]}

    #REPARTITION DES CARACTERISTIQUE DES PERSONNAGE AU DEBUT DE LA PARTIE
    def debut(self):
        self.name = input("Quel est votre nom ? : ")
        self.pv_physique = 20
        self.pv_mental = 10
        if personnage == "chevalier":
            self.force = 5
            self.eloquence = 10
            self.ruse = 5
            self.attaque = 5
            self.armure = 5
            self.pouvoir = 0
            self.argent = 20
            print("a")
        elif personnage == "voleur":
            self.force = 2
            self.eloquence = 3
            self.ruse = 10
            self.attaque = 7
            self.armure = 2
            self.pouvoir = 0
            self.argent = 5
            print("b")
        elif personnage == "sorcier":
            self.force = 4
            self.eloquence = 7
            self.ruse = 5
            self.attaque = 5
            self.armure = 3
            self.pouvoir = 6
            self.argent = 10
            print("c")

    #SELECTION DES ARMES, ARMURES, ET SORTS LORS DE LA PARTIE
    def selection(self, arme, armure, sort):

        choix = ""
        #choix des armes
        if arme is True:
            while (choix != "dague" and choix != "épée" and choix != "masse" and choix != "fléau"
                    and choix != "Master_Sword" and choix != "Mjölnir" and choix != "FROSTMOURNE"):
                choix = input("Choix d'arme : ")
                choix = choix.lower()
            if (choix == self.Armes.keys()[0] and self.Armes["épée"][2] > 0
                and self.Armes["épée"][3] <= self.force):
                self.arme = self.Armes["épée"]
            elif (choix == self.Armes.keys()[1] and self.Armes["FROSTMOURNE"][2] < 0
                and self.Armes["FROSTMOURNE"][3] <= self.force):
                self.arme = self.Armes["FROSTMOURNE"]
            elif (choix == self.Armes.keys()[2] and self.Armes["Mjölnir"][2] < 0
                and self.Armes["Mjölnir"][3] <= self.force):
                self.arme = self.Armes["Mjölnir"]
            elif (choix == self.Armes.keys()[3] and self.Armes["Master_Sword"][2] < 0
                and self.Armes["Master_Sword"][3] <= self.force):
                self.arme = self.Armes["Master_Sword"]
            elif (choix == self.Armes.keys()[4] and self.Armes["fléau"][2] < 0
                and self.Armes["fléau"][3] <= self.force):
                self.arme == self.Armes["fléau"]
            elif (choix == self.Armes.keys()[5] and self.Armes["masse"][2] < 0
                and self.Armes["masse"][3] <= self.force):
                self.arme == self.Armes["masse"]
            elif (choix == self.Armes.keys()[6] and self.Armes["dague"][2] < 0
                and self.Armes["dague"][3] <= self.force):
                self.arme == self.Armes["dague"]
            else :
                self.arme = []

        #choix des armures
        if armure is True :
            while (choix != self.Armures.keys()[0] and choix != self.Armures.keys()[1]
                   and choix != self.Armures.keys()[2] and choix != self.Armures.keys()[3]
                   and choix != self.Armures.keys()[4] and choix != self.Armures.keys()[5]
                   and choix != "rien") :
                choix = input("Choix d'armure : ")
                choix = choix.lower()
            if (choix == self.Armures.keys()[1] and self.Armures["gambison de cuir"][2] > 0
                and self.Armures["gambison de cuir"][3] <= self.cons) :
                self.armure = self.Armures["gambison de cuir"]
            elif (choix == self.Armures.keys()[2] and self.Armures["armure de fer"][2] > 0
                  and self.Armures["armure de fer"][3] <= self.cons) :
                self.armure = self.Armures["armure de fer"]
            elif (choix == self.Armures.keys()[0] and self.Armures["DAEDRIQUE"][2] > 0
                  and self.Armures["DAEDRIQUE"][3] <= self.cons) :
                self.armure = self.Armures["DAEDRIQUE"]
            elif (choix == self.Armures.keys()[3] and self.Armures["Bouclier_Hylien"][2] > 0
                  and self.Armures["Bouclier_Hylien"][3] <= self.cons) :
                self.armure = self.Armures["Bouclier_Hylien"]
            elif (choix == self.Armures.keys()[4] and self.Armures["Armure_ancestral"][2] > 0
                  and self.Armures["Armure_ancestral"][3] <= self.cons) :
                self.armure = self.Armures["Armure_ancestral"]
            elif (choix == self.Armures.keys()[5] and self.Armures["armure d'acier"][2] > 0
                  and self.Armures["armure d'acier"][3] <= self.cons) :
                self.armure = self.Armures["armure d'acier"]
            else :
                self.armure = [0]
            

        #choix des sorts
        if sort is True :
            while (choix != "boule de feu mineur" and choix != "boule de feu majeur"
                   and choix != "FLAMME" and choix != "TEMPUS"
                   and choix != "DEPRETIO"
                   and choix != "rien") :
                choix = input("Choix du sort : ")
                choix = choix.lower()
            if (choix == self.Sorts.keys()[0] and self.Sorts["boule de feu mineur"][2] > 0
                and self.Sorts["boule de feu mineur"][5] <= self.pouvoir) :
                self.sort = self.Sorts["boule de feu mineur"]
            elif (choix == self.Sorts.keys()[1] and self.Sorts["boule de feu majeur"][2] > 0
                  and self.Sorts["boule de feu majeur"][5] <= self.pouvoir) :
                self.sort = self.Sorts["boule de feu majeur"]
            elif (choix == self.Sorts.keys()[2] and self.Sorts["FLAMME"][2] > 0
                  and self.Sorts["FLAMME"][5] <= self.pouvoir) :
                self.sort = self.Sorts["FLAMME"]
            elif (choix == self.Sorts.keys()[3] and self.Sorts["TEMPUS"][2] > 0
                  and self.Sorts["TEMPUS"][5] <= self.pouvoir) :
                self.sort = self.Sorts["TEMPUS"]
            elif (choix == self.Sorts.keys()[4] and self.Sorts["DEPRETIO"][2] > 0
                  and self.Sorts["DEPRETIO"][5] <= self.pouvoir) :
                self.sort = self.Sorts["DEPRETIO"]
            else :
                self.sort = []

    #PREMIERE PARTIE DE L'INVENTAIRE DES PERSONNAGES
    def inventaire(self) :

        ratio = float(self.pv_physique)+float(self.pv_mental)
        if ratio == 30.0 :
            self.etat = "est en pleine forme"
        elif ratio >= 25.0 :
            self.etat = "est en forme"
        elif ratio >= 20 :
            self.etat = "a quelques blessures superficielles"
        elif ratio >= 12 :
            self.etat = "est blessé et a besoin de soins"
        else :
            self.etat = "est gravement blessé"
        print("")
        print (self.name,self.etat)
        print("### Argent :",self.argent,"Pièce d'or")
        print("Force :",self.force,"### Ruse :",self.ruse)
        for key,nb in self.Armes.items() :
            if nb[2] > 0 :
                print ("-",nb[2],key)
        for key,nb in self.Armures.items() :
            if nb[2] > 0 :
                print ("-",nb[2],key)
        for key,nb in self.Sorts.items() :
            if nb[4] > 0 :
                print ("-",nb[4],key)
        print("")

    #DEFINITION DES DIFFERENTS MODULES DES COMBATS
    def fight(self, nom, att, ca, vit, dex, pv, distance) :
        
        nb_recul = 1
        nb_recul_m = 2
        print ("Un",nom,"attaque")
        self.inventaire()
        self.selection(True,True,False)
        while pv > 0 and self.pv_physique > 0 :
            self.inventaire()
            print("Le",nom,"est �",distance,"m�tres de distance. Il a",pv,"pv")
            choix = ""
            while (choix != "avancer" and choix != "reculer" and choix != "rien"
                   and choix != "attaque" and choix != "sort") :
                choix = input("Que fais-tu? ")
            if choix == "avancer" and distance > self.vitesse :
                distance -= self.vitesse
            elif choix == "avancer" and distance <= self.vitesse :
                distance = 1
            elif choix == "reculer" and nb_recul > 0 :
                nb_recul -= 1
                distance += self.vitesse
            elif choix == "reculer" and nb_recul < 0 :
                print("Tu ne peux plus reculer")
            elif choix == "attaque" and distance == 1 :
                self.selection(1,0,0)
                toucher = randrange(1, 20)
                if toucher <= sdes :
                    pv -= self.arme[0]
                    print("Tu le frappes et lui inflige"),self.arme[0],"dégàts"
                else :
                    print("Tu le rates")
            elif choix == "attaque" and distance > 1 :
                print("Impossible tu es trop loin de la cible")
                choix = ""
            elif choix == "sort" :
                self.selection(False,False,True)
                if self.sort[2] <= distance :
                    if self.sort[1] == "att" :
                        pv -= self.sort[0]
                        print("Tu lances ce sort qui inflige",self.sort[0],"dégàts")
                    else :
                        choix = ""
                else :
                    print("Tu es trop pr�s pour pouvoir lancer ton sort")
                    choix = ""
                choix = ""
            else : ()
            if pv <= 0 :
                print("Tu as vaincu!")
                return True
            else :
                if distance > 1 and att < self.arme[0] and nb_recul_m > 0 :
                    print("Le",nom,"recule")
                    distance += vit
                    nb_recul_m -= 1
                elif (distance > 1 and att > self.arme[0]) or (distance > 1 and nb_recul_m == 0) :
                    print("Le",nom,"avance")
                    if vit > distance :
                        distance = 1
                    else :
                        distance -= vit
                elif distance == 1 :
                    toucher = randrange(1, 20)
                    if toucher <= sdes :
                        print("Il t'attaque et t'inflige",att,"points de dégàts")
                    else :
                        print("Il n'arrive pas à te toucher")
        if self.pva <= 0 :
            print("Il t'a tué!")
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
        print ("Les gardes vous attaquent")
        self.inventaire()
        self.selection(True,True,False)
        while pv > 0 and self.pv_physique > 0 :
            self.inventaire()
            print("Les gardes sont à ",distance,"mètres de distance. Ils",pv,"pv")
            choix = ""
            while (choix != "avancer" and choix != "reculer" and choix != "rien"
                   and choix != "attaque" and choix != "sort") :
                choix = input("Que fais-tu? ")
            if choix == "avancer" and distance > self.vitesse :
                distance -= self.vitesse
            elif choix == "avancer" and distance <= self.vitesse :
                distance = 1
            elif choix == "reculer" and nb_recul > 0 :
                nb_recul -= 1
                distance += self.vitesse
            elif choix == "reculer" and nb_recul < 0 :
                print("Tu ne peux plus reculer")
            elif choix == "attaque" and distance == 1 :
                self.selection(1,0,0)
                toucher = randrange(1, 20)
                if toucher <= sdes :
                    pv -= self.arme[0]
                    print("Tu le frappes et lui inflige"),self.arme[0],"dégàts"
                else :
                    print("Tu le rates")
            elif choix == "attaque" and distance > 1 :
                print("Impossible tu es trop loin de la cible")
                choix = ""
            elif choix == "sort" :
                self.selection(False,False,True)
                if self.sort[2] <= distance :
                    if self.sort[1] == "att" :
                        pv -= self.sort[0]
                        print("Tu lances ce sort qui inflige",self.sort[0],"dégàts")
                    else :
                        choix = ""
                else :
                    print("Tu es trop près pour pouvoir lancer ton sort")
                    choix = ""
                choix = ""
            else : ()
            if pv <= 0 :
                print("Tu as vaincu!")
                return True
            else :
                if distance > 1 and att < self.arme[0] and nb_recul_m > 0 :
                    print("Les guardes reculent")
                    distance += vit
                    nb_recul_m -= 1
                elif (distance > 1 and att > self.arme[0]) or (distance > 1 and nb_recul_m == 0) :
                    print("Les gardes avancent")
                    if vit > distance :
                        distance = 1
                    else :
                        distance -= vit
                elif distance == 1 :
                    toucher = randrange(1, 20)
                    if toucher <= sdes :
                        print("Ils t'attaquent et t'infligent",att,"points de dégàts")
                    else :
                        print("Ils n'arrivent pas à te toucher")
        if self.pva <= 0 :
            print("Ils t'ont tué!")
            return False
        else :
            return True

    
    def fight_dernier_guardien(self) : #combat contre le dernier guardien à Icegate
        
        print("")
        print("Vous entez une présence très poche juste derrière vous,")
        print("Vous distinguez à quelques mètres de vous un homme")
        print("de votre taille lourdement habillé, il se trouve dans l'ombre")
        print("et vous ne voyer pas son visage vous aller demander qui il est quand...")
        nb_recul = 1
        nb_recul_m = 2
        distance = 3
        pv = 25
        vit = 4
        att = 6
        print ("Il vous attaque")
        self.inventaire()
        self.selection(True,True,False)
        while pv > 0 and self.pv_physique > 0 :
            self.inventaire()
            print("Les gardes sont à ",distance,"mètres de distance. Ils",pv,"pv")
            choix = ""
            while (choix != "avancer" and choix != "reculer" and choix != "rien"
                   and choix != "attaque" and choix != "sort") :
                choix = input("Que fais-tu? ")
            if choix == "avancer" and distance > self.vitesse :
                distance -= self.vitesse
            elif choix == "avancer" and distance <= self.vitesse :
                distance = 1
            elif choix == "reculer" and nb_recul > 0 :
                nb_recul -= 1
                distance += self.vitesse
            elif choix == "reculer" and nb_recul < 0 :
                print("Tu ne peux plus reculer")
            elif choix == "attaque" and distance == 1 :
                self.selection(1,0,0)
                toucher = randrange(1, 20)
                if toucher <= sdes :
                    pv -= self.arme[0]
                    print("Tu le frappes et lui inflige"),self.arme[0],"dégàts"
                else :
                    print("Tu le rates")
            elif choix == "attaque" and distance > 1 :
                print("Impossible tu es trop loin de la cible")
                choix = ""
            elif choix == "sort" :
                self.selection(False,False,True)
                if self.sort[2] <= distance :
                    if self.sort[1] == "att" :
                        pv -= self.sort[0]
                        print("Tu lances ce sort qui inflige",self.sort[0],"dégàts")
                    else :
                        choix = ""
                else :
                    print("Tu es trop près pour pouvoir lancer ton sort")
                    choix = ""
                choix = ""
            else : ()
            if pv <= 0 :
                print("Tu as vaincu!")
                return True
            else :
                if distance > 1 and att < self.arme[0] and nb_recul_m > 0 :
                    print("Les guardes reculent")
                    distance += vit
                    nb_recul_m -= 1
                elif (distance > 1 and att > self.arme[0]) or (distance > 1 and nb_recul_m == 0) :
                    print("Les gardes avancent")
                    if vit > distance :
                        distance = 1
                    else :
                        distance -= vit
                elif distance == 1 :
                    toucher = randrange(1, 20)
                    if toucher <= sdes :
                        print("Ils t'attaquent et t'infligent",att,"points de dégàts")
                    else :
                        print("Ils n'arrivent pas à te toucher")
        if self.pva <= 0 :
            print("Ils t'ont tué!")
            return False
        else :
            return True


            


test = Perso()
test.debut()