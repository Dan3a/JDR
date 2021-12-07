
def f1(x):
    fx= 2*(x**3)-3*x-1
    return(fx)

borneinf = input("borneinf : ")
bornesup = input("bornesup : ")
pas = input("pas : ")

def f2(borneinf,bornesup,pas):
    x = borneinf
    while x < bornesup:
        print(f1(x))
        x = x + pas
    return()
print(f2(borneinf,bornesup,pas))

