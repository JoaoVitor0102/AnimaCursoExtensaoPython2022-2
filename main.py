# comando imput() permite que o usuário digite algo 

nome = input ("Digite seu Nome:")

#comando de saída.. exibir na tela
print (nome)
#usar o int pra utilizar inteiros 
idade = int(input ("qual sua idade?"))

print (f"sua idade é {idade} anos")

#mostrar o DOBRO da idade informada

dobro = idade * 2

print (f"o dobro da sua idade é {dobro} anos")

#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, pode dirigir

if (idade) >= 18:
  print ("você é adulto")
else:
  print ("você é criança")



sexo = input ("qual seu sexo?,M = masculino/ F= feminino:")


print (f"o seu sexo é {sexo}")

if (idade) >= 18 and (sexo) == "M":
  print("Aliste ao exército")
else:
  print("você é muié")
