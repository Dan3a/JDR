# exercice 2

from random import randint

n=0

while n<100:
    piece1=randint(1,2)
    piece2=randint(1,2)
    piece3=randint(1,2)
    piece4=randint(1,2)
    n=n+1
    if piece1==piece2==piece3==piece4:
        print("Vous avez gagné au bout de", n, "essais")
        break