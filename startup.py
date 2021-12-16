import click
from gameMenu import GameWindow
import classe_personnage_fix as AA

step = 0

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
def accepter():
    if step==0:
        fight_debut == True
        
@click.command()
def refuser():
    if step==0:
        fightRefus


cli.add_command(accepter)
cli.add_command(refuser)

# Pass the group, and optionally app_name="my app"
# tkinterify(cli, app_name="My functions")
GameWindow(cli)