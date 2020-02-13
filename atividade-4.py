valor1 = int(input("Digite 0 ou 1: "))
valor2 = int(input("Digite 0 ou 1: "))
valor3 = int(input("Digite 0 ou 1: "))

print("\n")
print(valor1,"AND",valor2,": ",bool(valor1) and bool(valor2))
print(valor1,"AND",valor3,": ",bool(valor1) and bool(valor3))
print(valor2,"OR",valor3,": ",bool(valor2) or bool(valor3))

print("\n")
print(valor1,"AND",valor2,"AND",valor3,": ",bool(valor1) and bool(valor2) and bool(valor3))
print("NOT", valor1,"OR", valor2,": ", not bool(valor1) or bool(valor2))
print("NOT", valor1, "OR NOT", valor3, ": ",not bool(valor1) or not bool(valor3))

print("\n")
print("(NOT",valor1,"OR",valor2,") AND",valor3,": ",(not bool(valor1) or bool(valor2)) and bool(valor3))
print("NOT",valor1,"AND NOT",valor2,"AND NOT",valor3,": ",not bool(valor1) and not bool(valor2) and not bool(valor3))
print("NOT(", valor1,"OR",valor2,"OR",valor3,")",": ", not (bool(valor1) or bool(valor2) or bool(valor3)))

print("\n")
print(valor1,"AND False:", bool(valor1) and False)
print(valor1, "AND NOT", valor1,":", bool(valor1) and not bool(valor1))
print(valor1, "OR NOT",valor1,":",bool(valor1) or not bool(valor1))