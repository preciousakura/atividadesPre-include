num = int(input("Digite um número: "))
inc = " incomodam"

if(num>0):
    for cont in range(1,(num+1)):
        if(cont==1):
            print(cont, "elefante incomoda muita gente")
        else:
            print(cont, "elefantes", inc*cont,"muito mais")

else:
    print("Seu número é negativo!")