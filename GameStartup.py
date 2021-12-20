import click
import chevalier as ch
from gameMenu import GameWindow
import classe_personnage_fix as AA

prologue = False
fight_debut = False
fight_dernier_guardien = False
sorcier = False
jeu_taverne = False
fight_souterrain = False
fightRefus=AA.Perso.fight_Refus


# You must add your commands to a group in order to use tkinterify
@click.group()
def cli():
    pass

# @click.command()
# def accepter_ordre():
#     if prologue == False:
#         fight_debut == True
#         print("Vous avez décidé de laisser mécontentement envers le Roi de côté")
#         print("et acceptez la mission. Les gardes repartent et vous partez en")
#         print("route vers la clairrière au centre du royaume.")
#         print("")
#         print("")
#         print("Vous arrivez dans la clairrière, lieu habituellement plein de vie,")
#         print("où toutes les histoires se raconte. Mais seul quelques personnes")
#         print("passent de temps en temps; vous devez essayer de savoir si des rumeurs")
#         print("circulent autour d'un voleur ou des crystaux.")
#         print("Commandes disponibles : interroger-un-passant; chemin-au-hazard")
#         state = 1
    
# @click.command()
# def refuser_ordre():
#     if prologue == True:
#         fightRefus
#         state = 1


@click.command()
def accepter_ordre():
    ch.choix_moral1 = True

@click.command()
def refuser_ordre():
    ch.choix_moral1 = False


cli.add_command(accepter_ordre)
cli.add_command(refuser_ordre)

# Pass the group, and optionally app_name="my app"
# tkinterify(cli, app_name="My functions")
GameWindow(cli)