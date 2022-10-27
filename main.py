#pede o número do aluno e sua nota (0 a 10) e se ele tirou nota 10, mostra "Você passou"

nome = input("informe seu nome:")
nota = float(input("digite sua nota"))

if(nota == 10):
  print(f"parabéns {nome}, você passou com gosto")

elif (nota >= 6 and nota <= 10):
  print("foi bom, mas podia ser melhor")

else:
  print("Não tirou 10")