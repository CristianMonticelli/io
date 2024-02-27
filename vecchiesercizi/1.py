numero_pasticcini = int(input("numero pasticcini:"))
numero_1 = numero_pasticcini//5
numero_1_resto = numero_pasticcini%5
numero_2 = numero_1_resto//3
numero_2_resto = numero_1_resto%3
numero_3 = numero_2_resto//1

print("scatole da 5:" + str(numero_1))
print("scatole da 3:" + str(numero_2))
print("scatole da 1:" + str(numero_3))