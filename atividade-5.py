print("-------------------------------------------------- DATA DE HOJE --------------------------------------------------")
diaDeHoje = int(input("Digite o dia de hoje: "))
mesDeHoje = int(input("Digite o mês de hoje: "))
anoDeHoje = int(input("Digite o ano de hoje: "))

print("-------------------------------------------------- DATA DO FUTURO --------------------------------------------------")

diaDoFut = int(input("Digite o dia do futuro: "))
mesDoFut = int(input("Digite o mês do futuro: "))
anoDoFut = int(input("Digite o ano do futuro: "))

qtsAnos = (anoDoFut-anoDeHoje)*360
qtsMeses= (mesDoFut-mesDeHoje)*30
qtsDias= (diaDoFut-diaDeHoje)

final = (qtsAnos + qtsMeses + qtsDias)
#print(qtsAnos)
#print(qtsMeses)
#print(qtsDias)
print("Faltam",final,"dias para chegar na sua data do futuro!")