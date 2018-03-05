# -*- coding: utf-8 -*-



'''Aula'''

# x=13
# if x%2 == 0:
#     print(x, "é par")
# else:
#     print(x, "é ímpar")


# tupla = ("a", "b", "c", "d", "e")
# type(tupla)
# t1 = ('a')
# type(t1)
# tupla = ('A',)+tupla[1:]

# x,y,z = 1,2,3
# print(x)
# print(y)
# print(z)
# x,y,z = y,z,x
# print(x)
# print(y)
# print(z)

# dicionario = {}
# type(dicionario)
# dicionario['one']='um'
# dicionario['two']='dois'
# print(dicionario)

# inventario = {"abacaxis": 430, "bananas": 312, "laranjas": 525, "peras": 217}
# print(inventario)
# del inventario["peras"]
# print(inventario)
# inventario["peras"] = 0
# print(inventario)
# print(len(inventario))
# #inventario. (comandos adicionais)
# print(inventario.get("abacaxis"))
# 'abacaxis' in inventario

# opposites = {"up": "down", "right": "wrong", "true": "false"}
# alias = opposites
# copy = opposites.copy()
# print(opposites)
# print (alias)
# print(copy)
# alias["right"] = "left"
# opposites["right"]
# print(opposites)
# print (alias)
# print(copy)
# copy["right"] = "privilege"
# opposites["right"]
# print(opposites)
# print (alias)
# print(copy)


'''Exercício 1'''

# x=int(input("Digite o valor do primeiro número: "))
# y=int(input("Digite o valor do segundo número: "))
#
# if x>y:
#     print(x, ', o primeiro número digitado, é o maior!')
# elif x<y:
#     print(y, ', o segundo número digitado, é o maior!')
# else:
#     print('Os dois números digitados são iguais!')


'''Exercício 2'''

# z = int(input("Digite o valor de um número: "))
# if z % 2 == 0 and z > 0:
#     print("O número é par e positivo!")
# elif z % 2 != 0 and z > 0:
#     print("O número é ímpar e positivo!")
# elif z % 2 == 0 and z < 0:
#     print("O número é par e negativo!")
# elif z % 2 != 0 and z < 0:
#     print("O número é ímpar e negativo!")
# else:
#     print("O número é zero!")

'''Exercício 3'''

# x = int(input("Digite o valor do primeiro número: "))
# y = int(input("Digite o valor do segundo número: "))
# z = int(input("Digite o valor do terceiro número: "))
#
# if x > y and y > z:
#     print(z, y, x)
# elif x > y and x < z:
#     print(x, y, z)
# elif x < y and x > z:
#     print(z, x, y)
# elif x > y and x < z:
#     print(y, x, z)
# elif z > y and z < x:
#     print(y, z, x)
# else:
#     print(x, z, y)

'''Exercício 4'''

# notas = {}
# notas['AB1'] = float(input("Digite o valor da primeira nota: "))
# notas['AB2'] = float(input("Digite o valor da segunda nota: "))
# notas['AB3'] = float(input("Digite o valor da terceira nota: "))
# notas['Media'] = (notas['AB1']+notas['AB2']+notas['AB3'])/3
# if notas['Media'] < 3:
#     notas['Situacao'] = 'Reprovado'
#     notas['Exige-se'] = 'Não se aplica'
# elif notas['Media'] >= 7:
#     notas['Situacao'] = 'Aprovado'
#     notas['Exige-se'] = 'Não se aplica'
# else:
#     notas['Situacao'] = 'Exame'
#     notas['Exige-se'] = 12 - notas['Media']
#
# print(notas)

'''Exercício 5'''

n = int(input("Digite o número de contatos da lista: "))
while n < 10:
    n = int(input("O número de contatos da lista deve ser, no mínimo, 10. Redigite-o: "))

print(n) #todo COMENTAR
lista = {}
r = [[0] for i in range(n)]
N = []

for i in range(0, n):
    a = raw_input("Digite o nome do contato: ")
    b = raw_input("Digite o telefone do contato: ")
    lista[a] = b
    r[i] = list(lista.keys()[i])

print ("A lista telefônica criada é: \n", lista)

# print(lista.values()[0])
# print(lista.values()[1])
# print(lista.values()[2])

for i in range(0, n):
    c = 0
    for j in range(i+1, n):
        if r[i] == r[j]:
            if lista.keys()[j] not in N:
                N.append(lista.keys()[j])
                print (r[i])
                print (r[j])
            c = c+1
        else:
            m = len(r[i])
            n = len(r[j])
            if m != n:
                pass
            else:
                e = 0
                for k in range(n):
                    if r[i][k] in r[j]:
                        e = e + 1
                    else:
                        break
                if e == n:
                    if lista.keys()[j] not in N:
                        N.append(lista.keys()[j])
                        print (r[i])
                        print (r[j])
                    c = c+1
    if c == 0:
        pass
    else:
        if lista.keys()[i] not in N:
            N.append(lista.keys()[i])
            print (r[i])
            print (r[j])


print("Nesta lista, são anagramas: ", N)

# for i in range(0, n):
#     N = [lista.keys()[i]]
#     c = 0
#     for j in range(i+1, n):
#         if r[i] == r[j]:
#             N = N+[lista.keys[j]]
#             c = c+1
#         else:
#             m = len(r[i])
#             n = len(r[j])
#             if m != n:
#                 pass
#             else:
#                 e = 0
#                 for k in range(n):
#                     if r[i][k] in r[j]:
#                         e = e + 1
#                     else:
#                         break
#                 if e == n:
#                     N = N + [lista.keys()[j]]
#                     c = c+1
#     if c == 0:
#         pass
#     else:
#         print("Nesta lista, são anagramas: ", N)