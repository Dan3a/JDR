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
        self.fight_dernier_guardien = False
        self.sorcier = False
        self.jeu_taverne = False
        self.fight_souterrain = False


        
    
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
                    self.fight_debut = AA.fight_Refus(self)
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
                    print("Vous remontez donc le royaume vers Icegate, cet endroit reculé")
                    print("de Dahal à la frontière avec le royaume énemi: Crézantis, ")
                    print("ednroit où le royaume garde précieusement ses trois crystaux")
                    print("")
                    print("A votre arrivé dans ce lieu habituellement rempli de garde, ")
                    print("vous n'etes acceuilli que par un vent glacé et un étrange présentiment")
                    self.place = 4
                elif choix == "interroger une autre personne" :
                    print("")
                    print("Vous portez que peu d'importance à cette dîte histoire,")
                    print("Vous ne trouvez pas important de se rendre aussi loin ")
                    print("pour confirmer cette rumeur. Mais un peu plus loin, ")
                    print("vous apercevez une autre personne, vous décider d'aller")
                    print("lui parler pour essayer d'avoir d'autre information.")
                    print("")
                    print("- Excusez moi Sir, est-ce que vous auriez entendu parler d'un voleur trainant dans les parrage?")
                    print("- Bonsoir à vous, en effet je suppose que c'est en rapport avec la nuit qui s'est abbatu sur le royaume")
                    print("- Il est vrai que cela est un lien, mais auriez vous des information sur ce qu'il s'est passé ?")
                    print("- Non, veuillez m'en excusez, je suis le vieux gardien des souterrains de Deadfalls je n'entend que peut de chose là bas.")
                    print("")
                    print("Vous aviez déjà entendu parler de ce vieux gardien,")
                    print("on raconte qu'il aurait les clés ouvrant les portes")
                    print("de ce fameux souterrain à Deadfalls, il y renfermerait")
                    print("Un monstre mythique mais également un incroyable trésor.")
                    print(" et vous savez que vous aurez besoin de ce tresor pour")
                    print("survire à cette aventure; il vous faut ces clés.")
                    self.place = 5

            while self.place == 3: #chemin hazard(Starhill)
                choix = ""
                while (choix != "rendre visite à cet ami" and choix != "revenir à la clairrière"):
                    choix = input("Que voulez-vous faire? ( rendre visite à cet ami/ revenir à la clairrière")
                    choix = choix.lower()
                if choix == "rendre visite à cet ami" :
                    print("")
                    print("Vous vous diriger vers sa demeure,")
                    print("vous ayant apperçut, il vous ouvre la porte.")
                    print("Cela fait plusieurs années que vous ne l'avez pas vu,")
                    print("vous le trouver changer, mais n'y prétant pas")
                    print("pas d'importance, vous entrez dans la maison")
                    print("Vous savez que vous ne devez pas tarder,")
                    print("le royaume court un grave danger, mais")
                    print("cette longue marche vous a fatiguée")
                    self.place = 6
                elif choix == "revenir à la clairrière" :
                    print("Vous avez un mauvais présage et préférer rentrer à la clairrière")
                    self.place = 1
                
            while self.place == 4: #aller à Icegate
                choix = ""
                while (choix != "chercher des traces du voleur" and choix != "regarder dans la montagne"
                        and choix != "aller voir les guardiens"):
                    choix = input("Que faites vous ? ( chercher des traces du voleur/ regarder dans la montagne/ aller voir les guardiens)")
                    choix = choix.lower()
                if choix == "chercher des traces du voleur" :
                    print("")
                    print("En fesant le tour de l'entrée, vous tomber")
                    print("sur des traces de pas, les traces s'enfoncent")
                    print("dans la neige en direction du Nord du royaume.")
                    print("Vous en etes certain, ce sont les traces du voleur")
                    print("vous décidez donc de les suivre.")
                    print("")
                    print("Vous arrivez dans la contrée de starhill lieu où peu de gens")
                    print("se rende en raison du peu d'intérêt de cette région,")
                    print("mais s'est également ici qu'habite un de vos ami.")
                    self.place = 3
                elif choix == "regarder dans la montagne" :
                    print("")
                    print("Les trois crystaux étant sensé être renfermer")
                    print("dans la montagne, vous décider d'aller y jeter")
                    print("un oeil, vous entrez à l'interieur et vous vous")
                    print("enfoncer au coeur de la grande salle, quand soudain...")
                    self.place = "combat_gardien"
                elif choix == "aller voir les guardiens" :
                    print("")
                    print("Après une longue exploration des lieux,")
                    print("vous etes forcé de constater que les ")
                    print("guardiens ont disparuent.")
                    choix2 =""
                    while (choix2 != "chercher dans la montagne" and choix2 != "trouver des traces du voleur"):
                        choix2 = input("Que souhaitez-vous faire? (chercher dans la montagne/ trouver des traces du voleur")
                        choix2 = choix2.lower()
                    if choix2 == "chercher dans la montagne" :
                        print("")
                        print("A la recherche des guardien vous vous aventurez")
                        print("dans la montagne, vous décider d'aller y jeter")
                        print("un oeil, vous entrez à l'interieur et vous vous")
                        print("enfoncer au coeur de la grande salle, quand soudain...")
                        self.place = "combat_gardien"
                    elif choix2 == "trouver des traces du voleur" :
                        print("")
                        print("En fesant le tour de l'entrée, vous tomber")
                        print("sur des traces de pas, les traces s'enfoncent")
                        print("dans la neige en direction du Nord du royaume.")
                        print("Vous en etes certain, ce sont les traces du voleur")
                        print("vous décidez donc de les suivre.")
                        print("")
                        print("Vous arrivez dans la contrée de starhill lieu où peu de gens")
                        print("se rende en raison du peu d'intérêt de cette région,")
                        print("mais s'est également ici qu'habite un de vos ami.")
                        self.place = 3

            while self.place == 5: #avoir les clés du vieux guardien
                choix =""
                while (choix != "menacer le vieu guardien" and choix != "amadouer le vieu guardien" and choix != "demander poliment"):
                    choix = input("Que faites-vous ? ( menacer le vieu guardien/ amadoué le vieu guardien/ demander poliment")
                    choix = choix.lower()
                if choix == "menacer le vieu guardien" :
                    print("")
                    print("Vous etes pressé, et vous ne voulez pas discuter plus longtemps,")
                    print("une folie vous emporte et vous menacer le guardien de votre dague.")
                    print("Ce dernier paniquer se tétanisé, après quelques secondes,")
                    print("vous remet faibrillement les clés avant de partir sans se retourner")
                    print("")
                    print("Comme vous avez enfin ces clés, vous vous rendez à Deadfalls,")
                    print("sur le chemin une lueure attire votre attention.")
                    choix2 = "" #suivre ou pas illusion
                    while (choix2 != "aller voir de plus près" and choix != "continuer vers Deadfalls"):
                        choix2 = input("Que choisissez-vous? ( aller voir de plus près/ continuer vers Deadfalls")
                        choix2 = choix.lower()
                    if choix2 == "aller voir de plus près":
                        print("")
                        print("Cette lueure vous intrigue et vous décidez de vous approcher.")
                        print("Au pied d'un arbre se trouve une petite fiole fluorenscente.")
                        choix3 = "" # boire ou pas -6 pv physique
                        while (choix3 != "repartir" and choix3 != "boire la fiole"):
                            choix3 = input("Que faites-vous? ( repartir/ boire la fiole)")
                            choix3 = choix.lower()
                        if choix3 == "repartir":
                            print("")
                            print("En y réfléchissant, vous songer que boire cette substance,")
                            print("n'est pas une bonne idée, vous décidez donc de continuer")
                            print("votre chemin vers Deadfalls et ses souterrains.")
                            print("")
                            print("Lorsque que vous arrivez, cette longue marche vous a fatigué,")
                            print("et une taverne se trouve près de l'entrée de Deadfalls.")
                            self.place = 7
                        elif choix3 == "boire la fiole":
                            print("")
                            print("")
                    elif choix2 == "continuer vers Deadfalls":
                        print("")
                        print("Vous continuer votre chemin vers Deadfalls pour enfin ouvrir ces souterrains.")
                        print("Mais où etes fatigué et une taverne se trouve non loin.")
                        self.place = 7
                elif choix == "amadoué le vieu guardien" :
                    print("")
                    print("Vous vous doutez que qu'il ne vous donnera les clés aussi facilement,")
                    print("vous lui proposez donc 10 PO en échange des clés, après réflexion")
                    print("Il vous remet les clés en échange de 20 PO, satisfait vous le saluez et repartez.")
                    print("Ayant enfin ces clés, vous vous rendez à Deadfalls pour ouvrir ces souterrains.")
                    print("Mais où etes fatigué et une taverne se trouve non loin.")
                    self.place = 7
                elif choix == "demander poliment" :
                    print("")
                    print("Vous avez confiance en votre incroyable capacité à vous exprimer,")
                    print("vous entamer une longue discussion en commencant à vous lié d'amitié")
                    print("avec cette personne, qui finira par vous céder volontier les clés.")
                    print("Ayant enfin ces clés, vous prenez le chemin Deadfalls pour ouvrir ces souterrains.")
                    print("Mais où etes fatigué et une taverne se trouve non loin.")
                    self.place = 7

            while self.place == 6: #rester chez ami ou pas
                choix = ""
                while (choix != "rester se reposer" and choix != "continuer les recherches"):
                    choix = input("Que voulez-vous faire? ( rester se reposer/ continuer les recherches")
                    choix = choix.lower()
                if choix == "rester se reposer":
                    print("")
                    print("Après une courte réflexion, vous vous dites qu'une nuit dans un bon")
                    print("lit ne vous fera pas de mal après autant de marche. Vous montez donc à l'étage")
                    print("vous alonger et commencer à sombrer dans un profond sommeil...")
                    print("")
                    print(".......")
                    print("")
                    print("De ce sommeil, vous ne vous réveillerais jamais et vous n'en saurait donc jamais la raison.")
                    self.place = 0

                elif choix == "continuer les recherches":
                    print("")
                    print("Vous décidez de na pas rester trop longtemps, et entamez avant de partir")
                    print("une petite discussion autour de ce qui pèse sur le royaume et vous essayez")
                    print("d'en savoir un peu plus. Au moment de vous quitter, votre ami vous apprendra")
                    print("que les crystaux ont étés créés par les sorciers de cet même contrée de Starhill.")
                    print("Vous décidez donc de vous rendre chez un des dernier sorcier habitant pas loin d'ici.")
                    print("")
                    print("Vous arrivez à sa demeure, quand la porte souvre d'un coup devant vous,")
                    print("vous entrez prudement quand un homme un peu barbu ariive en face de vous")
                    print("Vous vous appretez à lui parler quand il annoce qu'il sait qui vous êtes")
                    print("et pourquoi vous êtes là, il vous dis que se sont les personne comme")
                    print(" lui qui ont créés les trois crystaux il y a plusieur siècle et perssone")
                    print("n'a le droit d'y toucher encore moin de les voler.")
                    print("Vous lui annoncer que vous êtes à la recherche de cet individu et que vous n'allez")
                    print("pas rester, vous lui demandez si il n'aurait pas quelques informations")
                    print("qui vous seraient utiles, il vous répond d'un aire sombre qu'il ressent")
                    print("leur pouvoir en direction des côtes de Bayfort, vous décidez donc")
                    print("de vous y rendre et il vous demande il peut vous accompagné pour vous")
                    print("aider lors de votre combat.")
                    choix2 = "" #accepter ou refuser l'aide du sorcier
                    while (choix2 != "accepter son aide" and choix2 != "refuser son aide"):
                        choix2 = input("Que voulez-vous faire? ( accepter son aide/ refuser son aide")
                        choix2 = choix2.lower()
                    if choix2 == "accepter son aide":
                        print("")
                        print("Sans réfléchir, vous accepter son aide, vous ne savez pas qui est votre")
                        print("adversaire et ne savez donc pas de quoi il est capable, il vous parrait donc")
                        print("logique d'avoir avec vous une personne aussi puissante que le sorcier")
                        print("qui poursuit le même but que vous.")
                        print("Vous partez donc en direction de Bayfort accompagné de ce nouvel ami")
                        self.sorcier = True
                        self.place = 8
                    elif choix2 == "refuser son aide":
                        print("")
                        print("Vous ne savez pas ce qui vous arrivera arrivé à Bayfort et vous ne voulez")
                        print("pas qu'une autre personne puisse courir un risque aussi important, de plus")
                        print("vous ne connaissez que peu le sorcier et ne lui faites pas forcément confiance.")
                        print("En lui annoncant votre refus, il parait désolé et insite et présisant")
                        print("qu'il connait et maitrise le pouvoir des crystaux et qu'il est important")
                        print("pour lui de les retrouvé rapidement pour le bien du royaume...")
                        choix3 = "" #sorcier insiste choix
                        while (choix3 != "accpeter finalement son aide" and choix3 != "continuer à refuser poliment"):
                            choix3 = input("Que décidez-vous? ( accepter finalement son aide/ continuer à refuser poliment")
                            choix3 = choix3.lower()
                        if choix3 == "accepter finalement son aide":
                            print("")
                            print("Vous accepter finalement qu'il vienne avec vous, il ne peut que vous")
                            print("être utile et qu'il à les même intention que vous, vous partez")
                            print("donc tous les deux en direction de Bayfort.")
                            self.sorcier = True
                            self.place = 8
                        elif choix3 == "continuer à refuser poliment":
                            print("")
                            print("Vous lui dites avec toutes les précaution possible, que vous")
                            print("n'avez pas besoin de son aide et que préférez continuer seul.")
                            print("il vous regarde longuement avant de vous souhaiter bonne route,")
                            print("vous le saluez et partez donc seul en direction de Bayfort.")
                            self.sorcier = False
                            self.place = 8
                    

            while self.place == 7: #retourner à DeadFalls avec les clés
                choix = ""
                while (choix != "aller dans la taverne" and choix != "aller dans les souterrains"):
                    choix = input("Que choisissez-vous? ( aller dans la taverne/ aller dans les souterrains")
                    choix = choix.lower()
                if choix == "aller dans la taverne":
                    print("")
                    print("Vous vous sentez un peu fatigué et vous avez faim, vous vous rendez donc dans la")
                    print("taverne. Vous manger un petit peu et une table de jeu attire votre attention,")
                    print("vous décidez donc en grand amateur de jeu de chance de vous joindre à la partie.")
                    self.place = "jeu_taverne"
                elif choix == "aller dans les souterrains":
                    print("")
                    self.place = "souterrain"

            while self.place == 8: #forgeron avant bayfort
                print("")
                print("Sur votre route vers Bayfort, vous passez près de la boutique d'un forgeron")
                choix = ""
                while (choix != "rentrez dans la boutique"):
                    choix = input("Que faites-vous? ( aller dans la boutique )")
                    choix = choix.lower()
                if choix == "aller dans la boutique":
                    print("")
                    self.place = "boutique_forgeron"

            while self.place == "combat_gardien": #combat contre dernier guardien
                self.fight_dernier_guardien = AA.fight_dernier_guardien1(self)
                if self.fight_dernier_guardien is False:
                    print("")
                    self.place = 0
                else:
                    print("")
                    print("Votre énemi et à terre, avant de lui donner le coup fatal,")
                    print("vous décidez de voire son visage...")
                    print("Un peu défiguré mais vous le reconnaissez, c'est un guardien,")
                    print("un des guardiens des troix crystaux, immédiatement vous le relevez.")
                    print("Il vous explique alors ce qu'il s'est passé, un intru à pénétré")
                    print("dans la monbtagne et à voler les crystaux, personne ne l'avait")
                    print("repéré mais quand les gardiens ont couluent s'interposer lors de sa fuite,")
                    print("il a utilisé le pouvoir des crystaux, tous les guardiens")
                    print("y sont restés, lui a réussit à fuire et vous voyant pensant que c'était le voleur")
                    print("venu l'achevé, à voulu vous tué.")
                    print("Après avoir vous avoir conté son histoire, vous remarquer qu'il ne va pas bien")
                    print("il est blessé en plusieurs endroits, vous proposé de le ramener à Farville pour le soigner.")
                    print("Il refuse et vous pris d'aller arrêter l'intru, pour vous aider, il vous laisse")
                    print("les clés des souterrains de Deadfalls ou se trouverait un grand trésor et également")
                    print("une épée, une épée mythique des guardiens: FROSTMOURNE.")
                    print("vous décidez donc de continuer votre quête et de partir en direction de Deadfalls")
                    print("laissant le derniers des guardiens de Icegate succomber.")
                    print("")
                    print("Vous arrivé près des souterrains de Deadfalls vous vous sentez fatigué par ce combat.")
                    self.place = 7

            while self.place == "jeu_taverne": #jeu de chance code dans personnage
                print("")
                print("Vous vous approchez de la table pour y voir unn petit groupe de personne")
                print("à un jeu de dès peu commun.")
                choix = ""
                while (choix != "jouer au jeu"):
                    choix = input("Alors que faites-vous? ( jouer au jeu ) ")
                    choix = choix.lower()
                if choix == "jouer au jeu":
                    print("")
                    self.jeu_taverne = AA.jeu_taverne1(self)
                    if self.jeu_taverne is True:
                        print("")
                        print("Vous ressorter de la taverne en pleine forme, il ne vous reste")
                        print("plus qu'à oubrir les portes des souterrains, vous vous y dirigez")
                        print("d'un pas pressé mais en gardant en tête que le monstre sensé")
                        print("se trouver à l'interrieur est un des plus dangereux.")
                        self.place = "souterrain"

        while self.place == "souterrain": #combat et trésort dans souterrain à Deadfalls
            print("vous descendez de plus en plus prfofnd, dans une obscurité la plus total,")
            print("vous hésitez à abandonner et à remonter, mais vous pensez à quel point se")
            print("trésort si vous parvenez à atteindre peut être important dans votre quête.")
            print("D'un coup après plusieurs minutes dans un dédalle de galerie, vous débouchez")
            print("dans une immense caverne illuminée de plusieur cristaux...")
            self.fight_souterrain = AA.fight_souterrain1(self)
            if self.fight_souterrain is False:
                self.place = 0
            else:
                print("")
                print("")


             
