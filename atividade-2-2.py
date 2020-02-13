num = int(input("Digite um número: "))
seq = 0
ant = 1


if(num>0):
    for cont in range(num,0,-1):
        seq = ant + seq 
        ant = seq - ant
        
        print(seq)
else:
    print("Seu número é negativo!")