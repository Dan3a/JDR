#CH-1-Chevalier
from random import *

import classe_personnage_fix as AA

def jeu(mainWindow):
    perso = AA.Perso()
    perso.debut(mainWindow)
    place = 1
    prologue = False
    choix_moral1 = ""
    choix_moral2 = ""
    choix_moral3 = ""
    fight_debut = False
    fight_dernier_guardien = False
    sorcier = False
    jeu_taverne = False
    fight_souterrain = False
    

    while place > 0:

        while prologue is False:
            
            mainWindow.printInTextArea("Vous vous réveillez par un bruit de pas;")
            mainWindow.printInTextArea("le bruit de pas de gardes royaux au pied de votre porte.")
            mainWindow.printInTextArea("Vous vous levez, ouvrez la porte et un message vous est tendu : ")
            mainWindow.printInTextArea("*** Sir, le royaume court un grave danger, ***")
            mainWindow.printInTextArea("*** les 3 cristaux de Dahal ont été volé à Icegate. ***")
            mainWindow.printInTextArea("*** Le royaume est tombé dans une nuit éternelle ***")
            mainWindow.printInTextArea("*** où les monstres peuvent y refaire leur apparition. ***")
            mainWindow.printInTextArea("*** Par ordre du roi, vous devez les retrouver  ***")
            mainWindow.printInTextArea("*** et arrêter celui qui les a dérobés… ***")
            mainWindow.printInTextArea("Vous n'avez pas besoin d'en lire plus, vous saviez que cela allait arriver,")
            mainWindow.printInTextArea("et vous en savez le danger, mais vous vous rappelez également")
            mainWindow.printInTextArea("vos mauvaises relations récentes avec le Roi. Vous devez prendre une décision.")
            while choix_moral1 != "accepter l'ordre" and choix_moral1 != "refuser l'ordre" :
                choix_moral1 = mainWindow.waitForEntryText("Que faites vous ? (accepter l'ordre/ refuser l'ordre) ")
                choix_moral1 = choix_moral1.lower()

            if choix_moral1 == "refuser l'ordre":
                perso.fight_Refus()
            else:
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous avez décidé de laisser votre mécontentement envers le Roi de côté")
                mainWindow.printInTextArea("et acceptez la mission. Les gardes repartent et vous partez en")
                mainWindow.printInTextArea("route vers la clairrière au centre du royaume.")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous arrivez dans la clairrière, lieu habituellement plein de vie")
                mainWindow.printInTextArea("Où toutes les histoires se raconte. Mais seul quelques personnes")
                mainWindow.printInTextArea("passent de temps en temps; vous devez essayer de savoir si des rumeurs")
                mainWindow.printInTextArea("circulent autours d'un voleur ou des crystaux.")
                place = 1
                prologue = True
            # mainWindow.printInTextArea("")
            # if fight_debut is False:
            #     place = 0
            # else:
            #     if choix_moral1 == "accepter l'ordre" :
            #         mainWindow.printInTextArea("Vous avez décidé de laisser votre mécontentement envers le Roi de côté")
            #         mainWindow.printInTextArea("et acceptez la mission. Les gardes repartent et vous partez en")
            #         mainWindow.printInTextArea("route vers la clairrière au centre du royaume.")
            #         mainWindow.printInTextArea("")
            #         mainWindow.printInTextArea("")
            #         mainWindow.printInTextArea("Vous arrivez dans la clairrière, lieu habituellement plein de vie")
            #         mainWindow.printInTextArea("Où toutes les histoires se raconte. Mais seul quelques personnes")
            #         mainWindow.printInTextArea("passent de temps en temps; vous devez essayer de savoir si des rumeurs")
            #         mainWindow.printInTextArea("circulent autours d'un voleur ou des crystaux.")
            #         place = 1
            #     else:
            #         mainWindow.printInTextArea("")
                

        
        while place == 1 : #aller clairrière
            choix = ""
            while (choix != "interroger un passant" and choix != "prendre un chemin au hazard"):
                choix = mainWindow.waitForEntryText("Que faites vous ? ( interroger un passant/ prendre un chemin au hazard)")
                choix = choix.lower()
            if choix == "interroger un passant" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous interpellez une personne passant à côté de vous")
                mainWindow.printInTextArea("et lui demander si elle sait quelque chose : ")
                mainWindow.printInTextArea("Après un court échange et une longue réflexion, ")
                mainWindow.printInTextArea("Vous apprenez qu'une histoire circule disant")
                mainWindow.printInTextArea("que les crystaux ne se trouveraient plus à Icegate")
                place = 2
            elif choix == "prendre un chemin au hazard":
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Ne croisant que peu de personnes, vous décidez de prendre")
                mainWindow.printInTextArea("au hazard un des nombreux chemins partants de la clairrière.")
                mainWindow.printInTextArea("Vous arrivez dans la contrée de starhill lieu où peu de gens")
                mainWindow.printInTextArea("se rende en raison du peu d'intérêt de cette région,")
                mainWindow.printInTextArea("mais s'est également ici qu'habite un de vos ami.")
                place = 3

        while place == 2 : #demander passant
            choix = ""
            while (choix != "se rendre à icegate" and choix != "interroger une autre personne"):
                choix = mainWindow.waitForEntryText("Que faites vous ? ( se rendre à Icegate/ interroger une autre personne")
                choix = choix.lower()

            if choix == "se rendre à icegate" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous remontez donc le royaume vers Icegate, cet endroit reculé")
                mainWindow.printInTextArea("de Dahal à la frontière avec le royaume énemi: Crézantis, ")
                mainWindow.printInTextArea("endroit où le royaume garde précieusement ses trois crystaux")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("A votre arrivée dans ce lieu habituellement rempli de gardes, ")
                mainWindow.printInTextArea("vous n'êtes acceuillis que par un vent glacé et un étrange présentiment")
                place = 4
            elif choix == "interroger une autre personne" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous portez que peu d'importance à cette dîte histoire,")
                mainWindow.printInTextArea("Vous ne trouvez pas important de se rendre aussi loin ")
                mainWindow.printInTextArea("pour confirmer cette rumeur. Mais un peu plus loin, ")
                mainWindow.printInTextArea("vous apercevez une autre personne, vous décider d'aller")
                mainWindow.printInTextArea("lui parler pour essayer d'avoir d'autre information.")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("- Excusez moi Sir, est-ce que vous auriez entendu parler d'un voleur trainant dans les parrage?")
                mainWindow.printInTextArea("- Bonsoir à vous, en effet je suppose que c'est en rapport avec la nuit qui s'est abbatu sur le royaume")
                mainWindow.printInTextArea("- Il est vrai que cela est un lien, mais auriez vous des information sur ce qu'il s'est passé ?")
                mainWindow.printInTextArea("- Non, veuillez m'en excusez, je suis le vieux gardien des souterrains de Deadfalls je n'entend que peut de chose là bas.")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous aviez déjà entendu parler de ce vieux gardien,")
                mainWindow.printInTextArea("on raconte qu'il aurait les clés ouvrant les portes")
                mainWindow.printInTextArea("de ce fameux souterrain à Deadfalls, il y renfermerait")
                mainWindow.printInTextArea("Un monstre mythique mais également un incroyable trésor.")
                mainWindow.printInTextArea(" et vous savez que vous aurez besoin de ce tresor pour")
                mainWindow.printInTextArea("survire à cette aventure; il vous faut ces clés.")
                place = 5

        while place == 3: #chemin hazard(Starhill)
            choix = ""
            while (choix != "rendre visite à cet ami" and choix != "revenir à la clairrière"):
                choix = mainWindow.waitForEntryText("Que voulez-vous faire? ( rendre visite à cet ami/ revenir à la clairrière")
                choix = choix.lower()
            if choix == "rendre visite à cet ami" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous vous dirigez vers sa demeure,")
                mainWindow.printInTextArea("vous ayant apperçut, il vous ouvre la porte.")
                mainWindow.printInTextArea("Cela fait plusieurs années que vous ne l'avez pas vu,")
                mainWindow.printInTextArea("vous le trouver changer, mais n'y prétant pas")
                mainWindow.printInTextArea("pas d'importance, vous entrez dans la maison")
                mainWindow.printInTextArea("Vous savez que vous ne devez pas tarder,")
                mainWindow.printInTextArea("le royaume court un grave danger, mais")
                mainWindow.printInTextArea("cette longue marche vous a fatiguée")
                place = 6
            elif choix == "revenir à la clairrière" :
                mainWindow.printInTextArea("Vous avez un mauvais présage et préférer rentrer à la clairrière")
                place = 1
            
        while place == 4: #aller à Icegate
            choix = ""
            while (choix != "chercher des traces du voleur" and choix != "regarder dans la montagne"
                    and choix != "aller voir les guardiens"):
                choix = mainWindow.waitForEntryText("Que faites vous ? ( chercher des traces du voleur/ regarder dans la montagne/ aller voir les guardiens)")
                choix = choix.lower()
            if choix == "chercher des traces du voleur" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("En faisant le tour de l'entrée, vous tomber")
                mainWindow.printInTextArea("sur des traces de pas, les traces s'enfoncent")
                mainWindow.printInTextArea("dans la neige en direction du Nord du royaume.")
                mainWindow.printInTextArea("Vous en etes certain, ce sont les traces du voleur")
                mainWindow.printInTextArea("vous décidez donc de les suivre.")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous arrivez dans la contrée de starhill lieu où peu de gens")
                mainWindow.printInTextArea("se rende en raison du peu d'intérêt de cette région,")
                mainWindow.printInTextArea("mais s'est également ici qu'habite un de vos ami.")
                place = 3
            elif choix == "regarder dans la montagne" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Les trois crystaux étant sensé être renfermer")
                mainWindow.printInTextArea("dans la montagne, vous décider d'aller y jeter")
                mainWindow.printInTextArea("un oeil, vous entrez à l'interieur et vous vous")
                mainWindow.printInTextArea("enfoncer au coeur de la grande salle, quand soudain...")
                place = "combat_gardien"
            elif choix == "aller voir les guardiens" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Après une longue exploration des lieux,")
                mainWindow.printInTextArea("vous etes forcé de constater que les ")
                mainWindow.printInTextArea("guardiens ont disparuent.")
                choix2 =""
                while (choix2 != "chercher dans la montagne" and choix2 != "trouver des traces du voleur"):
                    choix2 = mainWindow.waitForEntryText("Que souhaitez-vous faire? (chercher dans la montagne/ trouver des traces du voleur")
                    choix2 = choix2.lower()
                if choix2 == "chercher dans la montagne" :
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("A la recherche des guardien vous vous aventurez")
                    mainWindow.printInTextArea("dans la montagne, vous décider d'aller y jeter")
                    mainWindow.printInTextArea("un oeil, vous entrez à l'interieur et vous vous")
                    mainWindow.printInTextArea("enfoncer au coeur de la grande salle, quand soudain...")
                    place = "combat_gardien"
                elif choix2 == "trouver des traces du voleur" :
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("En faisant le tour de l'entrée, vous tomber")
                    mainWindow.printInTextArea("sur des traces de pas, les traces s'enfoncent")
                    mainWindow.printInTextArea("dans la neige en direction du Nord du royaume.")
                    mainWindow.printInTextArea("Vous en etes certain, ce sont les traces du voleur")
                    mainWindow.printInTextArea("vous décidez donc de les suivre.")
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("Vous arrivez dans la contrée de starhill lieu où peu de gens")
                    mainWindow.printInTextArea("se rende en raison du peu d'intérêt de cette région,")
                    mainWindow.printInTextArea("mais s'est également ici qu'habite un de vos ami.")
                    place = 3

        while place == 5: #avoir les clés du vieux guardien
            choix =""
            while (choix != "menacer le vieu guardien" and choix != "amadouer le vieu guardien" and choix != "demander poliment"):
                choix = mainWindow.waitForEntryText("Que faites-vous ? ( menacer le vieu guardien/ amadoué le vieu guardien/ demander poliment")
                choix = choix.lower()
            if choix == "menacer le vieu guardien" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous etes pressé, et vous ne voulez pas discuter plus longtemps,")
                mainWindow.printInTextArea("une folie vous emporte et vous menacer le guardien de votre dague.")
                mainWindow.printInTextArea("Ce dernier paniquer se tétanisé, après quelques secondes,")
                mainWindow.printInTextArea("vous remet faibrillement les clés avant de partir sans se retourner")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Comme vous avez enfin ces clés, vous vous rendez à Deadfalls,")
                mainWindow.printInTextArea("sur le chemin une lueure attire votre attention.")
                choix2 = "" #suivre ou pas illusion
                while (choix2 != "aller voir de plus près" and choix != "continuer vers Deadfalls"):
                    choix2 = mainWindow.waitForEntryText("Que choisissez-vous? ( aller voir de plus près/ continuer vers Deadfalls")
                    choix2 = choix.lower()
                if choix2 == "aller voir de plus près":
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("Cette lueure vous intrigue et vous décidez de vous approcher.")
                    mainWindow.printInTextArea("Au pied d'un arbre se trouve une petite fiole fluorenscente.")
                    choix3 = "" # boire ou pas -6 pv physique
                    while (choix3 != "repartir" and choix3 != "boire la fiole"):
                        choix3 = mainWindow.waitForEntryText("Que faites-vous? ( repartir/ boire la fiole)")
                        choix3 = choix.lower()
                    if choix3 == "repartir":
                        mainWindow.printInTextArea("")
                        mainWindow.printInTextArea("En y réfléchissant, vous songez que boire cette substance,")
                        mainWindow.printInTextArea("n'est pas une bonne idée, vous décidez donc de continuer")
                        mainWindow.printInTextArea("votre chemin vers Deadfalls et ses souterrains.")
                        mainWindow.printInTextArea("")
                        mainWindow.printInTextArea("Lorsque que vous arrivez, cette longue marche vous a fatigué,")
                        mainWindow.printInTextArea("et une taverne se trouve près de l'entrée de Deadfalls.")
                        place = 7
                    elif choix3 == "boire la fiole":
                        mainWindow.printInTextArea("")
                        mainWindow.printInTextArea("")
                elif choix2 == "continuer vers Deadfalls":
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("Vous continuer votre chemin vers Deadfalls pour enfin ouvrir ces souterrains.")
                    mainWindow.printInTextArea("Mais où etes fatigué et une taverne se trouve non loin.")
                    place = 7
            elif choix == "amadoué le vieu guardien" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous vous doutez que qu'il ne vous donnera les clés aussi facilement,")
                mainWindow.printInTextArea("vous lui proposez donc 10 PO en échange des clés, après réflexion")
                mainWindow.printInTextArea("Il vous remet les clés en échange de 20 PO, satisfait vous le saluez et repartez.")
                mainWindow.printInTextArea("Ayant enfin ces clés, vous vous rendez à Deadfalls pour ouvrir ces souterrains.")
                mainWindow.printInTextArea("Mais où etes fatigué et une taverne se trouve non loin.")
                place = 7
            elif choix == "demander poliment" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous avez confiance en votre incroyable capacité à vous exprimer,")
                mainWindow.printInTextArea("vous entamer une longue discussion en commencant à vous lié d'amitié")
                mainWindow.printInTextArea("avec cette personne, qui finira par vous céder volontier les clés.")
                mainWindow.printInTextArea("Ayant enfin ces clés, vous prenez le chemin Deadfalls pour ouvrir ces souterrains.")
                mainWindow.printInTextArea("Mais où etes fatigué et une taverne se trouve non loin.")
                place = 7

        while place == 6: #rester chez ami ou pas
            choix = ""
            while (choix != "rester se reposer" and choix != "continuer les recherches"):
                choix = mainWindow.waitForEntryText("Que voulez-vous faire? ( rester se reposer/ continuer les recherches")
                choix = choix.lower()
            if choix == "rester se reposer":
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Après une courte réflexion, vous vous dites qu'une nuit dans un bon")
                mainWindow.printInTextArea("lit ne vous fera pas de mal après autant de marche. Vous montez donc à l'étage")
                mainWindow.printInTextArea("vous alonger et commencer à sombrer dans un profond sommeil...")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea(".......")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("De ce sommeil, vous ne vous réveillerais jamais et vous n'en saurait donc jamais la raison.")
                place = 0

            elif choix == "continuer les recherches":
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous décidez de na pas rester trop longtemps, et entamez avant de partir")
                mainWindow.printInTextArea("une petite discussion autour de ce qui pèse sur le royaume et vous essayez")
                mainWindow.printInTextArea("d'en savoir un peu plus. Au moment de vous quitter, votre ami vous apprendra")
                mainWindow.printInTextArea("que les crystaux ont étés créés par les sorciers de cet même contrée de Starhill.")
                mainWindow.printInTextArea("Vous décidez donc de vous rendre chez un des dernier sorcier habitant pas loin d'ici.")
                mainWindow.printInTextArea("")
                place = 10

        while place == 10: #chez le sorcier
                mainWindow.printInTextArea("Vous arrivez à la demeure du sorcier, quand la porte souvre d'un coup devant vous,")
                mainWindow.printInTextArea("vous entrez prudement quand un homme un peu barbu ariive en face de vous")
                mainWindow.printInTextArea("Vous vous appretez à lui parler quand il annoce qu'il sait qui vous êtes")
                mainWindow.printInTextArea("et pourquoi vous êtes là, il vous dis que se sont les personne comme")
                mainWindow.printInTextArea(" lui qui ont créés les trois crystaux il y a plusieur siècle et perssone")
                mainWindow.printInTextArea("n'a le droit d'y toucher encore moin de les voler.")
                mainWindow.printInTextArea("Vous lui annoncer que vous êtes à la recherche de cet individu et que vous n'allez")
                mainWindow.printInTextArea("pas rester, vous lui demandez si il n'aurait pas quelques informations")
                mainWindow.printInTextArea("qui vous seraient utiles, il vous répond d'un aire sombre qu'il ressent")
                mainWindow.printInTextArea("leur pouvoir en direction des côtes de Bayfort, vous décidez donc")
                mainWindow.printInTextArea("de vous y rendre et il vous demande il peut vous accompagné pour vous")
                mainWindow.printInTextArea("aider lors de votre combat.")
                choix2 = "" #accepter ou refuser l'aide du sorcier
                while (choix2 != "accepter son aide" and choix2 != "refuser son aide"):
                    choix2 = mainWindow.waitForEntryText("Que voulez-vous faire? ( accepter son aide/ refuser son aide")
                    choix2 = choix2.lower()
                if choix2 == "accepter son aide":
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("Sans réfléchir, vous accepter son aide, vous ne savez pas qui est votre")
                    mainWindow.printInTextArea("adversaire et ne savez donc pas de quoi il est capable, il vous parrait donc")
                    mainWindow.printInTextArea("logique d'avoir avec vous une personne aussi puissante que le sorcier")
                    mainWindow.printInTextArea("qui poursuit le même but que vous.")
                    mainWindow.printInTextArea("Vous partez donc en direction de Bayfort accompagné de ce nouvel ami")
                    sorcier = True
                    place = 8
                elif choix2 == "refuser son aide":
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("Vous ne savez pas ce qui vous arrivera arrivé à Bayfort et vous ne voulez")
                    mainWindow.printInTextArea("pas qu'une autre personne puisse courir un risque aussi important, de plus")
                    mainWindow.printInTextArea("vous ne connaissez que peu le sorcier et ne lui faites pas forcément confiance.")
                    mainWindow.printInTextArea("En lui annoncant votre refus, il parait désolé et insite et présisant")
                    mainWindow.printInTextArea("qu'il connait et maitrise le pouvoir des crystaux et qu'il est important")
                    mainWindow.printInTextArea("pour lui de les retrouvé rapidement pour le bien du royaume...")
                    choix3 = "" #sorcier insiste choix
                    while (choix3 != "accpeter finalement son aide" and choix3 != "continuer à refuser poliment"):
                        choix3 = mainWindow.waitForEntryText("Que décidez-vous? ( accepter finalement son aide/ continuer à refuser poliment")
                        choix3 = choix3.lower()
                    if choix3 == "accepter finalement son aide":
                        mainWindow.printInTextArea("")
                        mainWindow.printInTextArea("Vous accepter finalement qu'il vienne avec vous, il ne peut que vous")
                        mainWindow.printInTextArea("être utile et qu'il à les même intention que vous, vous partez")
                        mainWindow.printInTextArea("donc tous les deux en direction de Bayfort.")
                        sorcier = True
                        place = 8
                    elif choix3 == "continuer à refuser poliment":
                        mainWindow.printInTextArea("")
                        mainWindow.printInTextArea("Vous lui dites avec toutes les précaution possible, que vous")
                        mainWindow.printInTextArea("n'avez pas besoin de son aide et que préférez continuer seul.")
                        mainWindow.printInTextArea("il vous regarde longuement avant de vous souhaiter bonne route,")
                        mainWindow.printInTextArea("vous le saluez et partez donc seul en direction de Bayfort.")
                        sorcier = False
                        place = 8
                

        while place == 7: #retourner à DeadFalls avec les clés
            choix = ""
            while (choix != "aller dans la taverne" and choix != "aller dans les souterrains"):
                choix = mainWindow.waitForEntryText("Que choisissez-vous? ( aller dans la taverne/ aller dans les souterrains")
                choix = choix.lower()
            if choix == "aller dans la taverne":
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous vous sentez un peu fatigué et vous avez faim, vous vous rendez donc dans la")
                mainWindow.printInTextArea("taverne. Vous manger un petit peu et une table de jeu attire votre attention,")
                mainWindow.printInTextArea("vous décidez donc en grand amateur de jeu de chance de vous joindre à la partie.")
                place = "jeu_taverne"
            elif choix == "aller dans les souterrains":
                mainWindow.printInTextArea("")
                place = "souterrain"

        while place == 8: #forgeron avant bayfort
            mainWindow.printInTextArea("")
            mainWindow.printInTextArea("Sur votre route vers Bayfort, vous passez près de la boutique d'un forgeron")
            choix = ""
            while (choix != "rentrer dans la boutique"):
                choix = mainWindow.waitForEntryText("Que faites-vous? ( rentrer dans la boutique )")
                choix = choix.lower()
            if choix == "rentrer dans la boutique":
                mainWindow.printInTextArea("")
                place = "boutique_forgeron"

        while place == "combat_gardien": #combat contre dernier guardien
            fight_dernier_guardien = perso.fight_dernier_guardien1()
            if fight_dernier_guardien is False:
                mainWindow.printInTextArea("")
                place = 0
            else:
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Votre énemi et à terre, avant de lui donner le coup fatal,")
                mainWindow.printInTextArea("vous décidez de voire son visage...")
                mainWindow.printInTextArea("Un peu défiguré mais vous le reconnaissez, c'est un guardien,")
                mainWindow.printInTextArea("un des guardiens des troix crystaux, immédiatement vous le relevez.")
                mainWindow.printInTextArea("Il vous explique alors ce qu'il s'est passé, un intru à pénétré")
                mainWindow.printInTextArea("dans la monbtagne et à voler les crystaux, personne ne l'avait")
                mainWindow.printInTextArea("repéré mais quand les gardiens ont couluent s'interposer lors de sa fuite,")
                mainWindow.printInTextArea("il a utilisé le pouvoir des crystaux, tous les guardiens")
                mainWindow.printInTextArea("y sont restés, lui a réussit à fuire et vous voyant pensant que c'était le voleur")
                mainWindow.printInTextArea("venu l'achevé, à voulu vous tué.")
                mainWindow.printInTextArea("Après avoir vous avoir conté son histoire, vous remarquer qu'il ne va pas bien")
                mainWindow.printInTextArea("il est blessé en plusieurs endroits, vous proposé de le ramener à Farville pour le soigner.")
                mainWindow.printInTextArea("Il refuse et vous pris d'aller arrêter l'intru, pour vous aider, il vous laisse")
                mainWindow.printInTextArea("les clés des souterrains de Deadfalls ou se trouverait un grand trésor et également")
                mainWindow.printInTextArea("une épée, une épée mythique des guardiens: FROSTMOURNE.")
                mainWindow.printInTextArea("vous décidez donc de continuer votre quête et de partir en direction de Deadfalls")
                mainWindow.printInTextArea("laissant le derniers des guardiens de Icegate succomber.")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous arrivé près des souterrains de Deadfalls vous vous sentez fatigué par ce combat.")
                place = 7

        while place == "jeu_taverne": #jeu de chance code dans personnage
            mainWindow.printInTextArea("")
            mainWindow.printInTextArea("Vous vous approchez de la table pour y voir unn petit groupe de personne")
            mainWindow.printInTextArea("à un jeu de dès peu commun.")
            choix = ""
            while (choix != "jouer au jeu"):
                choix = mainWindow.waitForEntryText("Alors que faites-vous? ( jouer au jeu ) ")
                choix = choix.lower()
            if choix == "jouer au jeu":
                mainWindow.printInTextArea("")
                jeu_taverne = perso.jeu_taverne1()
                if jeu_taverne is True:
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("Vous ressorter de la taverne en pleine forme, il ne vous reste")
                    mainWindow.printInTextArea("plus qu'à oubrir les portes des souterrains, vous vous y dirigez")
                    mainWindow.printInTextArea("d'un pas pressé mais en gardant en tête que le monstre sensé")
                    mainWindow.printInTextArea("se trouver à l'interrieur est un des plus dangereux.")
                    place = "souterrain"

        while place == "souterrain": #combat et trésort dans souterrain à Deadfalls
            mainWindow.printInTextArea("vous descendez de plus en plus prfofnd, dans une obscurité la plus total,")
            mainWindow.printInTextArea("vous hésitez à abandonner et à remonter, mais vous pensez à quel point se")
            mainWindow.printInTextArea("trésort si vous parvenez à atteindre peut être important dans votre quête.")
            mainWindow.printInTextArea("D'un coup après plusieurs minutes dans un dédalle de galerie, vous débouchez")
            mainWindow.printInTextArea("dans une immense caverne illuminée de plusieur cristaux...")
            fight_souterrain = perso.fight_souterrain1()
            if fight_souterrain is False:
                place = 0
            else:
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("L'immense créature gisant à côté de vous, vous découvrez derrière lui")
                mainWindow.printInTextArea("un renfocement dans le quel se trouve un amocellement des plusieurs centaines")
                mainWindow.printInTextArea("de pièces d'or vous en emporter un maximum, puis vous sortez de cet horrible")
                mainWindow.printInTextArea("souterrain emportant également avec vous une écaille de l'immense reptile.")
                mainWindow.printInTextArea("Vous souhaitez repartir à la recherche du voleur, vous pouvez aller à Lostpoint")
                mainWindow.printInTextArea("pour échanger votre écaille chez un marabou en échange de potion spéciale.")
                choix2 = ""#aller à lostpoint
                while (choix2 != "aller à lostpoint"):
                    choix2 = mainWindow.waitForEntryText("Que faites-vous? ( aller à lostpoint )")
                    choix2 = choix2.lower()
                if choix2 == "aller à lostpoint":
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("Vous vous rendez donc à Lostpoint")
                    mainWindow.printInTextArea("Une fois arrivé là bas, vous entrez chez le marabou qui vous échange")
                    mainWindow.printInTextArea("votre écaille contre une étrange potion, il vous indique qu'en la buvant,")
                    mainWindow.printInTextArea("vous pourrez choissir entre rétablir votre vie ou augmenter votre force.")
                    mainWindow.printInTextArea("une fois sortie de chez cet étrange personnage, vous décidez d'interroger")
                    mainWindow.printInTextArea("quelque personne au sujet de votre quête, deux choses reviennent souvent:")
                    mainWindow.printInTextArea("quelques rumeures disent que le voleur aurait été appercut en direction de Bayfort")
                    mainWindow.printInTextArea("d'autre personne vous ont dis d'aller voir le sorcier à Starhill qui pourras")
                    mainWindow.printInTextArea("surement vous aider.")
                    place = 9
                    
        while place == 9: #voir sorcier ou directement Bayfort
            choix = ""
            while (choix != "aller à bayfort" and choix != "aller chez ce sorcier"):
                choix = mainWindow.waitForEntryText("Que décidez-vous? ( aller à bayfort/ aller chez ce sorcier)")
                choix = choix.lower()
            if choix == "aller à bayfort":
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous préférez ne pas perde de temps est partez directement en direction")
                mainWindow.printInTextArea("de Bayfort vers les côtes du royaume sur les traces du voleur.")
                place = 11
            elif choix == "aller chez ce sorcier":
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous préférez demander conseil au sorcier car les sorcier sont")
                mainWindow.printInTextArea("réputés pour leur grand savoir sur le royaume, vous partez donc")
                mainWindow.printInTextArea("vers Starhill.")
                place = 10



            
