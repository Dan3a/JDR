import click
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

@click.command()
def accepter_ordre():
    if prologue == True:
        fight_debut == True
        print("Vous avez décidé de laisser mécontentement envers le Roi de côté")
        print("et acceptez la mission. Les gardes repartent et vous partez en")
        print("route vers la clairrière au centre du royaume.")
        print("")
        print("")
        print("Vous arrivez dans la clairrière, lieu habituellement plein de vie,")
        print("où toutes les histoires se raconte. Mais seul quelques personnes")
        print("passent de temps en temps; vous devez essayer de savoir si des rumeurs")
        print("circulent autour d'un voleur ou des crystaux.")
        print("Commandes disponibles : interroger-un-passant; chemin-au-hazard")
        state = 1
    
@click.command()
def refuser_ordre():
    if prologue == True:
        fightRefus
        state = 1

@click.command()
def interroger_un_passant():
    print("Vous interpellez une personne passant à côté de vous")
    print("et lui demander si elle sait quelque chose : ")
    print("Après un court échange et une longue réflexion, ")
    print("Vous apprenez qu'une histoire circule disant")
    print("que les crystaux ne se trouveraient plus à Icegate")


@click.command()
def chemin_au_hazard():
    print("Ne croisant que peu de personnes, vous décidez de prendre")
    print("au hazard un des nombreux chemins partants de la clairrière.")
    print("Vous arrivez dans la contrée de starhill lieu où peu de gens")
    print("se rende en raison du peu d'intérêt de cette région,")
    print("mais s'est également ici qu'habite un de vos ami.")
        
    

cli.add_command(accepter_ordre)
cli.add_command(refuser_ordre)
cli.add_command(interroger_un_passant)
cli.add_command(chemin_au_hazard)

# Pass the group, and optionally app_name="my app"
# tkinterify(cli, app_name="My functions")
GameWindow(cli)