#exo 6
from random import *
n=1
d=0
e=0
while n<1001:
    a=randint(1,8)
    b=randint(1,8)
    print(a,b,end=" ")
    if a+b==2:
        d=d+1
    elif a+b==12:
        e=e+1
    n=n+1
x=d*100/1000
y=e*100/1000
print("le total 2 est sorti : ",d," fois et le total 12 est sorti : ",e," fois")
print("il y a : ",x,"pourcent de chance d'avoir 2 et : ",y,"pourcent de chance d'avoir 12")
