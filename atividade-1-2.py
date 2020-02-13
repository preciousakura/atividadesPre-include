a = int(input("Digite o coeficiente A: "))
b = int(input("Digite o coeficiente B: "))
c = int(input("Digite o coeficiente C: "))

delta = (b**2) - (4*a*c)
if(delta<0):
    print("Sua equação não possui raiz real")

elif(delta>0):
    raiz1 = (- b + delta**(1/2))/2*a
    raiz2 = (- b - delta**(1/2))/2*a
    if(raiz1>0 and raiz2>0):
        print("Suas raízes são", raiz1, "e", raiz2)
    elif(raiz1>0 and raiz2<0):
        print("A sua única raiz real é", raiz1)
    else:
        print("A sua única raiz real é", raiz2)
else:
    raiz1 = - b + delta**(1/2)
    print("Suas raízes é", raiz1)