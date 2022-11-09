print("aula 3 laços ")

contador = 1

while(contador <= 10):
  print (contador)
  contador = contador+1 #contador +=1

#laço for (python for = for each)
fruta = "morango"
print (fruta + "\n")

fruta1 = "morango"
fruta2 = "banana"
fruta3 = "laranja"

#lista
frutas = ["morango", "laranja", "banana"]

#mostra todos
print(frutas)

#mostrar determinado elemento em uma posição na lista (3a banana)
print(frutas[2])

#exibir quantos elementos tem na lista
print(len(frutas)) #length = tamanho

print("\n")

#incluir elemento na lista (fruta nova)
frutas.append("manga")

print(frutas)
print(len(frutas))

print("\n")

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
#print(frutas[4])

print("\n")

i=0
while(i<len(frutas)):
  print(frutas[i])
  i = i+1

print("\n")


print("Exemplos com for")
for fruta in frutas:
  print(fruta)