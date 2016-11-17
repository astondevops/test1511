#!/usr/bin/python3


# import de la lib sys
import sys

print(sys.version_info)
print(sys.version)

print(sys.platform)

print("Hello")
print('Hello')
print("c'est")
print("""  texte

       a la suite""")
print("c'est le texte dans C:\\user")

strAdresse = "Spam"
print (strAdresse)

a = [ 'a', 'b','c','d','e','f','g','h']
print (a[:4])
print(a[-4:])
print(a[3:-3])

i = 5
mykey= "temps"
fois = 20
print ('la valeur %d et le mot \'%s\' apparaissent %d fois.' % (i, mykey, fois))
print('la valeur {} et le mot \'{}\' appraissent {} fois'.format(i, mykey, fois))

valeur = "toto"
valeur2= "titi"
if valeur == "toto" and valeur2 == "titi" :
    print ("ok")

seq = [1,2,3,4]
a,b,c,d= seq
print (a)

for letter in "Spam":
    print ("current letter", letter)


fruits = ['banane','pomme','mangue']
for fruit in fruits:
    if fruit == "banane" :
        print (fruit[2])
    print (" mon fruit" , fruit)

for num in range(1,10):
     print (num)
     if num == 5:
         continue
     if num == 7 :
         break

var = 10
while True:
    var -=1
    if var == 6:
        continue
    print (var)
    if var == 0:
        break
print ("end loop")

a = [1,2,3,4,5,6,7,8,9,10]
squares = [x**2 for x in a]
print (squares)

# on a deux variables temps et distance
temps=6.896
distance=19.7
vitesse= distance/temps
#affichage formatte
msg="la vitesse est = {:.2f} metre par seconde"
print(msg.format(vitesse))
# en utilisant la fonction range
# afficher les entiers de 0 a 3
for i in range(0,4):
    print (i)
# autre afficher de 4 a 7
for i in range (0,10):
    if i > 3:
        print ("---" , i)
    if i == 7:
        break


# avec une boucle afficher les caracteres de la chaine suivante
msg= "c'est la formation Devops"
for c in msg:
    print (c)

# sur la liste suivante faire les actions suivantes
liste = [17,38,10,25,72]
# triez et affichez la liste
liste.sort()
print(liste)
# ajouter l'element 12 et afficher la liste
liste.append(12)
print(liste)
# affichez l'indice de l'element 17
print (liste.index(17))
# enlevez l'element 38 et afficher la liste
liste.remove(38)
print(liste)
# afficher la sous-liste du 3eme element jusqu'a la fin de la liste
print(liste[2:])













































