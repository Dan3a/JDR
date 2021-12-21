# Copyright 2021, Dan3A, rremi0     Contact : 21985756+Dan3a@users.noreply.github.com

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

from random import *

import classe_personnage_fix as AA

def jeu(mainWindow):
    perso = AA.Perso()
    perso.debut(mainWindow)
    place = 1
    prologue = False
    choix_moral1 = ""
    fight_debut = False
    fight_dernier_gardien = False
    sorcier = False
    jeu_taverne = False
    fight_souterrain = False
    combat_final1 = False
    combat_final2 = False
    boutique_forgeron = False

    

    while place > 0:

        while prologue is False:
            
            mainWindow.printInTextArea("")
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
            mainWindow.printInTextArea("et vous en savez le danger, mais vous vous rappelez également de vos")
            mainWindow.printInTextArea("mauvaises relations récentes avec le Roi. Vous devez prendre une décision.")
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
                mainWindow.printInTextArea("Vous arrivez dans la clairrière, lieu habituellement plein de vie,")
                mainWindow.printInTextArea("où toutes les histoires se racontent. Mais seul quelques personnes")
                mainWindow.printInTextArea("passent de temps en temps; vous devez essayer de savoir si des rumeurs")
                mainWindow.printInTextArea("circulent autour d'un voleur ou des crystaux.")
                place = 1
                prologue = True
                

        
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
                mainWindow.printInTextArea("au hazard un, des nombreux chemins partants de la clairrière.")
                mainWindow.printInTextArea("Vous arrivez dans la contrée de starhill lieu où peu de gens")
                mainWindow.printInTextArea("se rendent en raison du peu d'intérêt de cette région,")
                mainWindow.printInTextArea("mais c'est également ici qu'habite un de vos ami.")
                place = 3

        while place == 2 : #demander passant
            choix = ""
            while (choix != "se rendre à icegate" and choix != "interroger une autre personne"):
                choix = mainWindow.waitForEntryText("Que faites vous ? ( se rendre à Icegate/ interroger une autre personne")
                choix = choix.lower()

            if choix == "se rendre à icegate" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous remontez donc le royaume vers Icegate, cet endroit reculé")
                mainWindow.printInTextArea("de Dahal qui jusque-là gardait les trois crystaux précieusement,")
                mainWindow.printInTextArea("et qui se trouve à la frontière avec le royaume ennemi, Crézantis.")
                # mainWindow.printInTextArea("de Dahal à la frontière avec le royaume ennemi: Crézantis, ")
                # mainWindow.printInTextArea("endroit où le royaume garde précieusement ses trois crystaux")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("A votre arrivée dans ce lieu habituellement rempli de gardes, ")
                mainWindow.printInTextArea("vous n'êtes acceuillis que par un vent glacé et un étrange présentiment.")
                place = 4
            elif choix == "interroger une autre personne" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous portez que peu d'importance à cette dîte histoire,")
                mainWindow.printInTextArea("Vous ne trouvez pas important de se rendre aussi loin ")
                mainWindow.printInTextArea("pour confirmer cette rumeur. Mais un peu plus loin, ")
                mainWindow.printInTextArea("vous apercevez une autre personne, vous décider d'aller")
                mainWindow.printInTextArea("lui parler afin d'obtenir plus d'informations.")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("- Excusez moi Sir, est-ce que vous auriez entendu parler d'un voleur trainant dans les parrages?")
                mainWindow.printInTextArea("- Bonsoir à vous, en effet je suppose que c'est en rapport avec la nuit qui s'est abbatu sur le royaume")
                mainWindow.printInTextArea("- Il est vrai que cela est un lien, mais auriez-vous des information sur ce qu'il s'est passé ?")
                mainWindow.printInTextArea("- Non, veuillez m'en excusez, je suis le vieux gardien des souterrains de Deadfalls je n'entend que peu de chose là bas.")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous aviez déjà entendu parler de ce vieux gardien,")
                mainWindow.printInTextArea("on raconte qu'il aurait les clefs ouvrant les portes")
                mainWindow.printInTextArea("de ce fameux souterrain à Deadfalls, il y renfermerait")
                mainWindow.printInTextArea("un monstre mythique mais également un incroyable trésor.")
                mainWindow.printInTextArea("Vous savez que vous aurez besoin de ce tresor pour")
                mainWindow.printInTextArea("survire à cette aventure; il vous faut ces clefs.")
                place = 5

        while place == 3: #chemin hazard(Starhill)
            choix = ""
            while (choix != "rendre visite à cet ami" and choix != "revenir à la clairrière"):
                choix = mainWindow.waitForEntryText("Que voulez-vous faire? ( rendre visite à cet ami/ revenir à la clairrière )")
                choix = choix.lower()
            if choix == "rendre visite à cet ami" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous vous dirigez vers sa demeure,")
                mainWindow.printInTextArea("vous ayant apperçu, il vous ouvre la porte.")
                mainWindow.printInTextArea("Cela fait plusieurs années que vous ne l'avez pas vu,")
                mainWindow.printInTextArea("vous le retrouvez changé, mais n'y prétant")
                mainWindow.printInTextArea("pas d'importance, vous entrez dans la maison.")
                mainWindow.printInTextArea("Vous savez que vous ne devez pas tarder,")
                mainWindow.printInTextArea("le royaume court un grave danger, mais")
                mainWindow.printInTextArea("cette longue marche vous a fatiguée.")
                place = 6
            elif choix == "revenir à la clairrière" :
                mainWindow.printInTextArea("Vous avez un mauvais présage et préférez rentrer à la clairrière")
                place = 1
            
        while place == 4: #aller à Icegate
            choix = ""
            while (choix != "chercher des traces du voleur" and choix != "regarder dans la montagne"
                    and choix != "aller voir les gardiens"):
                choix = mainWindow.waitForEntryText("Que faites vous ? ( chercher des traces du voleur/ regarder dans la montagne/aller voir les gardiens)")
                choix = choix.lower()
            if choix == "chercher des traces du voleur" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("En faisant le tour de l'entrée, vous tombez")
                mainWindow.printInTextArea("sur des traces de pas, les traces s'enfoncent")
                mainWindow.printInTextArea("dans la neige en direction du Nord du royaume.")
                mainWindow.printInTextArea("Vous en êtes certain, ce sont les traces du voleur.")
                mainWindow.printInTextArea("Vous décidez donc de les suivre.")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous arrivez dans la contrée de starhill, lieu où peu de gens")
                mainWindow.printInTextArea("se rendent en raison du peu d'intérêt de cette région,")
                mainWindow.printInTextArea("mais c'est également ici qu'habite un de vos ami.")
                place = 3
            elif choix == "regarder dans la montagne" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Les trois crystaux étant sensé être renfermés")
                mainWindow.printInTextArea("dans la montagne, vous décidez d'aller y jeter")
                mainWindow.printInTextArea("un oeil, vous entrez à l'interieur et vous vous")
                mainWindow.printInTextArea("enfoncez au coeur de la grande salle, quand soudain...")
                place = "combat_gardien"
            elif choix == "aller voir les gardiens" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Après une longue exploration des lieux,")
                mainWindow.printInTextArea("vous êtes forcés de constater que les ")
                mainWindow.printInTextArea("gardiens ont disparu.")
                choix2 =""
                while (choix2 != "chercher dans la montagne" and choix2 != "trouver des traces du voleur"):
                    choix2 = mainWindow.waitForEntryText("Que souhaitez-vous faire? (chercher dans la montagne/ trouver des traces du voleur)")
                    choix2 = choix2.lower()
                if choix2 == "chercher dans la montagne" :
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("A la recherche des gardiens vous vous aventurez")
                    mainWindow.printInTextArea("dans la montagne, vous décidez d'aller y jeter")
                    mainWindow.printInTextArea("un coup œil, vous entrez à l'interieur et vous vous")
                    mainWindow.printInTextArea("enfoncez au cœur de la grande salle, quand soudain...")
                    place = "combat_gardien"
                elif choix2 == "trouver des traces du voleur" :
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("En faisant le tour de l'entrée, vous tombez")
                    mainWindow.printInTextArea("sur des traces de pas, les traces s'enfoncent")
                    mainWindow.printInTextArea("dans la neige en direction du Nord du royaume.")
                    mainWindow.printInTextArea("Vous en êtes certain, ce sont les traces du voleur.")
                    mainWindow.printInTextArea("Vous décidez donc de les suivre.")
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("Vous arrivez dans la contrée de starhill lieu où peu de gens")
                    mainWindow.printInTextArea("se rendent en raison du peu d'intérêt de cette région,")
                    mainWindow.printInTextArea("mais c'est également ici qu'habite un de vos ami.")
                    place = 3

        while place == 5: #avoir les clefs du vieux gardien
            choix =""
            while (choix != "menacer le vieux gardien" and choix != "amadouer le vieu gardien" and choix != "demander poliment"):
                choix = mainWindow.waitForEntryText("Que faites-vous ? ( menacer le vieux gardien/ amadouer le vieux gardien/        demander poliment)")
                choix = choix.lower()
            if choix == "menacer le vieux gardien" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous êtes pressé, et vous ne voulez pas discuter plus longtemps,")
                mainWindow.printInTextArea("une folie vous emporte et vous menacez le gardien avec votre dague.")
                mainWindow.printInTextArea("Ce dernier paniqué et tétanisé, vous remet fébrilement après quelques")
                mainWindow.printInTextArea("secondes les clefs avant de partir sans se retourner")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Comme vous avez enfin ces clefs, vous vous rendez à Deadfalls,")
                mainWindow.printInTextArea("sur le chemin une lueur attire votre attention.")
                choix2 = "" #suivre ou pas illusion
                while (choix2 != "aller voir de plus près" and choix != "continuer vers Deadfalls"):
                    choix2 = mainWindow.waitForEntryText("Que choisissez-vous? ( aller voir de plus près/ continuer vers Deadfalls)")
                    choix2 = choix.lower()
                if choix2 == "aller voir de plus près":
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("Cette lueur vous intrigue et vous décidez de vous approcher.")
                    mainWindow.printInTextArea("Au pied d'un arbre se trouve une petite fiole fluorescente.")
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
                elif choix2 == "continuer vers Deadfalls":
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("Vous continuez votre chemin vers Deadfalls pour enfin ouvrir ces souterrains.")
                    mainWindow.printInTextArea("Mais où êtes fatigué et une taverne se trouve non loin.")
                    place = 7
            elif choix == "amadouer le vieu gardien" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous vous doutez qu'il ne vous donnera les clefs aussi facilement,")
                mainWindow.printInTextArea("vous lui proposez donc 10 PO en échange des clefs. Après réflexion,")
                mainWindow.printInTextArea("il vous remet les clefs en échange de 20 PO, satisfait vous le saluez et repartez.")
                mainWindow.printInTextArea("Ayant enfin ces clefs, vous vous rendez à Deadfalls pour ouvrir ces souterrains.")
                mainWindow.printInTextArea("Mais où êtes fatigué et une taverne se trouve non loin.")
                place = 7
            elif choix == "demander poliment" :
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous avez confiance en votre incroyable capacité à vous exprimer,")
                mainWindow.printInTextArea("vous entamez une longue discussion en commençant à vous lier d'amitié")
                mainWindow.printInTextArea("avec cette personne, qui finira par vous céder volontier les clefs.")
                mainWindow.printInTextArea("Ayant enfin ces clefs, vous prenez le chemin Deadfalls pour ouvrir ces souterrains.")
                mainWindow.printInTextArea("Mais où êtes fatigué et une taverne se trouve non loin.")
                place = 7

        while place == 6: #rester chez ami ou pas
            choix = ""
            while (choix != "rester se reposer" and choix != "continuer les recherches"):
                choix = mainWindow.waitForEntryText("Que voulez-vous faire? ( rester se reposer/ continuer les recherches)")
                choix = choix.lower()
            if choix == "rester se reposer":
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Après une courte réflexion, vous vous dites qu'une nuit dans un bon")
                mainWindow.printInTextArea("lit ne vous fera pas de mal après autant de marche. Vous montez donc à l'étage")
                mainWindow.printInTextArea("vous alonger et commencez à sombrer dans un profond sommeil...")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea(".......")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("De ce sommeil, vous ne vous réveillerez jamais et vous n'en saurez donc jamais la raison.")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("VOUS ÊTES MORT")
                mainWindow.printInTextArea("FIN PAISIBLE")
                place = 0

            elif choix == "continuer les recherches":
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous décidez de ne pas rester trop longtemps. Vous entamez avant de partir")
                mainWindow.printInTextArea("une petite discussion autour de ce qui pèse sur le royaume et vous essayez")
                mainWindow.printInTextArea("d'en savoir un peu plus. Au moment de vous quitter, votre ami vous apprendra")
                mainWindow.printInTextArea("que les crystaux ont étés créés par les sorciers de cet même contrée de Starhill.")
                mainWindow.printInTextArea("Vous décidez de vous rendre chez un des dernier sorcier habitant non loin d'ici.")
                mainWindow.printInTextArea("")
                place = 10

        while place == 10: #chez le sorcier
                mainWindow.printInTextArea("Vous arrivez à la demeure du sorcier, lorsque la porte s'ouvre d'un coup devant vous,")
                mainWindow.printInTextArea("vous entrez prudemment, quand soudainement un homme un peu barbu arrive en face de vous.")
                mainWindow.printInTextArea("Vous vous apprêtez à lui parler quand il annonce qu'il sait qui vous êtes")
                mainWindow.printInTextArea("et pourquoi vous êtes là, il vous dit que se sont les personne comme")
                mainWindow.printInTextArea("lui qui ont créé les trois crystaux il y a plusieurs siècles et personne")
                mainWindow.printInTextArea("n'a le droit d'y toucher et encore moins de les voler.")
                mainWindow.printInTextArea("Vous lui annoncer que vous êtes à la recherche de cet individu et que vous n'alliez")
                mainWindow.printInTextArea("pas rester. Vous lui demandez s'il n'aurait pas quelques informations")
                mainWindow.printInTextArea("qui vous seraient utiles, il vous répond d'un aire sombre qu'il ressent")
                mainWindow.printInTextArea("leur pouvoir en direction des côtes de Bayfort, vous décidez donc")
                mainWindow.printInTextArea("de vous y rendre et il vous demande s'il peut vous accompagner.")
                mainWindow.printInTextArea("aider lors de votre combat.")
                choix2 = "" #accepter ou refuser l'aide du sorcier
                while (choix2 != "accepter son aide" and choix2 != "refuser son aide"):
                    choix2 = mainWindow.waitForEntryText("Que voulez-vous faire? (accepter son aide/ refuser son aide)")
                    choix2 = choix2.lower()
                if choix2 == "accepter son aide":
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("Sans réfléchir, vous acceptez son aide, vous ne savez pas qui est votre")
                    mainWindow.printInTextArea("adversaire et ne savez donc pas de quoi il est capable, il vous paraît donc")
                    mainWindow.printInTextArea("logique d'avoir avec vous une personne aussi puissante que le sorcier,")
                    mainWindow.printInTextArea("qui poursuit le même but que vous.")
                    mainWindow.printInTextArea("Vous partez donc en direction de Bayfort accompagné de ce nouvel coéquipier.")
                    sorcier = True
                    place = 8
                elif choix2 == "refuser son aide":
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("Vous ne savez pas ce qui vous arrivera à Bayfort et vous ne voulez")
                    mainWindow.printInTextArea("pas qu'une autre personne puisse courir un risque aussi important, de plus")
                    mainWindow.printInTextArea("vous ne connaissez que peu le sorcier et ne lui faites pas forcément confiance.")
                    mainWindow.printInTextArea("En lui annonçant votre refus, il paraît désolé et insiste en précisant")
                    mainWindow.printInTextArea("qu'il connait et maitrise le pouvoir des crystaux et qu'il est important")
                    mainWindow.printInTextArea("pour lui de les retrouver rapidement pour le bien du royaume...")
                    choix3 = "" #sorcier insiste choix
                    while (choix3 != "accpeter finalement son aide" and choix3 != "continuer à refuser poliment"):
                        choix3 = mainWindow.waitForEntryText("Que décidez-vous? (accepter finalement son aide/ continuer à refuser poliment")
                        choix3 = choix3.lower()
                    if choix3 == "accepter finalement son aide":
                        mainWindow.printInTextArea("")
                        mainWindow.printInTextArea("Vous acceptez finalement qu'il vienne avec vous, il ne peut que vous")
                        mainWindow.printInTextArea("être utile puisqu'il a les même intentions que vous.")
                        mainWindow.printInTextArea("Vous partez donc tous les deux en direction de Bayfort.")
                        sorcier = True
                        place = 8
                    elif choix3 == "continuer à refuser poliment":
                        mainWindow.printInTextArea("")
                        mainWindow.printInTextArea("Vous lui dites avec toutes les précaution possible, que vous")
                        mainWindow.printInTextArea("n'avez pas besoin de son aide et que préférez continuer seul.")
                        mainWindow.printInTextArea("Il vous regarde longuement avant de vous souhaiter bonne route,")
                        mainWindow.printInTextArea("vous le saluez et partez donc seul en direction de Bayfort.")
                        sorcier = False
                        place = 8
                

        while place == 7: #retourner à DeadFalls avec les clefs
            choix = ""
            while (choix != "aller dans la taverne" and choix != "aller dans les souterrains"):
                choix = mainWindow.waitForEntryText("Que choisissez-vous? (aller dans la taverne/ aller dans les souterrains)")
                choix = choix.lower()
            if choix == "aller dans la taverne":
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous vous sentez un peu fatigué et vous avez faim, vous vous rendez donc dans la")
                mainWindow.printInTextArea("taverne. Vous mangez un petit peu et une table de jeu attire votre attention,")
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

        while place == "combat_gardien": #combat contre dernier gardien
            fight_dernier_gardien = perso.fight_dernier_gardien1()
            if fight_dernier_gardien is False:
                mainWindow.printInTextArea("")
                place = 0
            else:
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Votre ennemi est à terre. Avant de lui donner le coup fatal,")
                mainWindow.printInTextArea("vous décidez de voir son visage...")
                mainWindow.printInTextArea("Il est un peu défiguré mais vous le reconnaissez, c'est un gardien,")
                mainWindow.printInTextArea("un des gardiens des troix crystaux, immédiatement vous le relevez.")
                mainWindow.printInTextArea("Il vous explique alors ce qu'il s'est passé: un intru a pénétré")
                mainWindow.printInTextArea("dans la montagne et a volé les crystaux, personne ne l'avait")
                mainWindow.printInTextArea("repéré mais lorsque les gardiens ont voulus s'interposer lors de sa fuite,")
                mainWindow.printInTextArea("il a utilisé le pouvoir des crystaux. Tous les autres gardiens")
                mainWindow.printInTextArea("y sont restés, lui a réussi à fuire et vous voyant pensant que c'était le voleur")
                mainWindow.printInTextArea("venu l'achever, a voulu vous tué.")
                mainWindow.printInTextArea("Après vous avoir conté son histoire, vous remarquez qu'il ne va pas bien.")
                mainWindow.printInTextArea("Il est blessé en plusieurs endroits, vous proposez de le ramener à Farville pour le soigner.")
                mainWindow.printInTextArea("Il refuse et vous prie d'aller arrêter le voleur. Pour vous aider, il vous laisse")
                mainWindow.printInTextArea("les clefs des souterrains de Deadfalls, où se trouverait un grand trésor et également")
                mainWindow.printInTextArea("une épée; l'épée mythique des gardiens: FROSTMOURNE.")
                mainWindow.printInTextArea("Vous décidez donc de continuer votre quête et de partir en direction de Deadfalls,")
                mainWindow.printInTextArea("laissant le dernier gardien d'Icegate succomber.")
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous arrivez près des souterrains de Deadfalls. Vous vous sentez fatigué par ce combat.")
                place = 7

        while place == "jeu_taverne": #jeu de chance code dans personnage
            mainWindow.printInTextArea("")
            mainWindow.printInTextArea("Vous vous approchez de la table pour y voir un petit groupe de personnes")
            mainWindow.printInTextArea("jouant à un jeu de dès peu commun.")
            choix = ""
            while (choix != "jouer au jeu"):
                choix = mainWindow.waitForEntryText("Alors que faites-vous? ( jouer au jeu ) ")
                choix = choix.lower()
            if choix == "jouer au jeu":
                mainWindow.printInTextArea("")
                jeu_taverne = perso.jeu_taverne1()
                if jeu_taverne is True:
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("Vous ressortez de la taverne en pleine forme, il ne vous reste")
                    mainWindow.printInTextArea("plus qu'à ouvrir les portes des souterrains. Vous vous y dirigez")
                    mainWindow.printInTextArea("d'un pas pressé mais en gardant en tête que le monstre sensé")
                    mainWindow.printInTextArea("se trouver à l'intérieur est un des plus dangereux.")
                    place = "souterrain"

        while place == "souterrain": #combat et trésort dans souterrain à Deadfalls
            mainWindow.printInTextArea("Vous descendez de plus en plus profond, dans l'obscurité la plus totale,")
            mainWindow.printInTextArea("vous hésitez à abandonner et à remonter, mais vous pensez à quel point ce")
            mainWindow.printInTextArea("trésor peut être important dans votre quête si vous parvenez à l'atteindre.")
            mainWindow.printInTextArea("Après plusieurs minutes dans un dédalle de galerie, vous débouchez")
            mainWindow.printInTextArea("dans une immense caverne illuminée de plusieurs cristaux...")
            fight_souterrain = perso.fight_souterrain1()
            if fight_souterrain is False:
                place = 0
            else:
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("L'immense créature gisant à côté de vous, vous découvrez derrière lui")
                mainWindow.printInTextArea("un renfoncement dans lequel se trouve un amoncellement des plusieurs centaines")
                mainWindow.printInTextArea("de pièces d'or. Vous en emportez un maximum, puis vous sortez de cet horrible")
                mainWindow.printInTextArea("souterrain emportant également avec vous une écaille de l'immense reptile.")
                mainWindow.printInTextArea("Vous souhaitez repartir à la recherche du voleur, vous pouvez aller à Lostpoint")
                mainWindow.printInTextArea("pour échanger votre écaille chez un marabou en échange d'une potion spéciale.")
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
                    mainWindow.printInTextArea("une fois sorti de chez cet étrange personnage, vous décidez d'interroger")
                    mainWindow.printInTextArea("quelques personne au sujet de votre quête, deux choses reviennent souvent:")
                    mainWindow.printInTextArea("quelques rumeures disent que le voleur aurait été apperçu en direction de Bayfort")
                    mainWindow.printInTextArea("d'autre personnes vous ont dis d'aller voir le sorcier à Starhill qui pourra")
                    mainWindow.printInTextArea("sûrement vous aider.")
                    place = 9
                    
        while place == 9: #voir sorcier ou directement Bayfort
            choix = ""
            while (choix != "aller à bayfort" and choix != "aller chez ce sorcier"):
                choix = mainWindow.waitForEntryText("Que décidez-vous? ( aller à bayfort/ aller chez ce sorcier)")
                choix = choix.lower()
            if choix == "aller à bayfort":
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous préférez ne pas perdre de temps est partez directement en direction")
                mainWindow.printInTextArea("de Bayfort vers les côtes du royaume sur les traces du voleur.")
                place = 8
            elif choix == "aller chez ce sorcier":
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous préférez demander conseil au sorcier car ils sont")
                mainWindow.printInTextArea("réputés pour leur grand savoir sur le royaume, vous partez donc")
                mainWindow.printInTextArea("vers Starhill.")
                place = 10

        while place == 11: #bataille final:
            if sorcier == False: #sans l'aide du sorcier
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous arrivez à l'entrée du pont menant à Bayfort, vous apercevez dans")
                mainWindow.printInTextArea("la pénombre de l'autre côté une silhouette s'arreter de courir en")
                mainWindow.printInTextArea("direction des bateaux pour désormais vous faire face.")
                mainWindow.printInTextArea("Vous êtes sûr, c'est bien la personne que vous traquez depuis tout ce temps,")
                mainWindow.printInTextArea("sans hésitation, arme à la main vous traversez le pont pour le combat")
                mainWindow.printInTextArea("qui vous permettra de récupérer les crystaux du royaume.")
                mainWindow.printInTextArea("Arrivé à la moitié du pont, vous vous arrêtez net, le voleur vient de sortir")
                mainWindow.printInTextArea("de son sac un des trois crystaux...")
                combat_final1 = perso.combat_final1
                if combat_final1 is False: #combat perdu
                    mainWindow.printInTextArea("")
                    place = 0
                else: #combat gagné
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("Epuisé, et blessé, vous regardez votre ennemi gisant face contre terre,")
                    mainWindow.printInTextArea("vous allez enfin pouvoir ramener les crystaux à Icegate et sauver le royaume.")
                    mainWindow.printInTextArea("Après toute cette traque, vous souhaitez enfin découvrir le visage de votre")
                    mainWindow.printInTextArea("énemi, vous vous avancez pour le relever quand quelque chose attire votre")
                    mainWindow.printInTextArea("regard vous levez les yeux et vous voyez de l'autre côté du pont, une homme,")
                    mainWindow.printInTextArea("un homme un peu barbu. Au moment où vous alliez lui demander qui il était et")
                    mainWindow.printInTextArea("pourquoi il était là, sans avoir eu le temps de réagir, une boule de feu traversant")
                    mainWindow.printInTextArea("le pont à plein vitesse vous aveugle avant de vous frapper en pleine poitrine.")
                    mainWindow.printInTextArea("Sous le choc et la douleur, vous tombez à terre; vos yeux commencent à se fermer,")
                    mainWindow.printInTextArea("avant de sombrer dans un sommeil éternel, vous appercevez à travers vos yeux")
                    mainWindow.printInTextArea("mi-clos: cet homme se pencher et récupérer les crystaux vavnt de dire ce mot:")
                    mainWindow.printInTextArea("-Enfin.")
                    place = "fin1"
            elif sorcier == True: #avec l'aide du sorcier
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Vous et le sorcier arrivez à l'entrée du pont menant à Bayfort, vous apercevez dans")
                mainWindow.printInTextArea("la pénombre de l'autre côté une silhouette s'arreter de courir en")
                mainWindow.printInTextArea("direction des bateaux pour désormais vous faire face.")
                mainWindow.printInTextArea("Vous êtes sûr, c'est bien la personne que vous traquez depuis tout ce temps,")
                mainWindow.printInTextArea("sans hésitation, arme à la main, à vous deux vous traversez le pont pour le combat")
                mainWindow.printInTextArea("qui vous permettra de récupérer les crystaux du royaume.")
                mainWindow.printInTextArea("arrivés à la moitié du pont, vous vous arrêtez net, le voleur vient de sortir")
                mainWindow.printInTextArea("de son sac un des trois crystaux...")
                combat_final2 = perso.combat_final2
                if combat_final2 is False: #combat perdu
                    mainWindow.printInTextArea("")
                    place = 0
                else: #combat gagné
                    mainWindow.printInTextArea("")
                    mainWindow.printInTextArea("")


        while place == "boutique_forgeron": #boutique forgeron achat arme et armure
            boutique_forgeron = perso.boutique_forgeron1
            if boutique_forgeron == True:
                mainWindow.printInTextArea("")
                mainWindow.printInTextArea("Après être sortie de la boutique, vous pouvez enfin vous rendre à Bayfort.")
                place = 11

            
