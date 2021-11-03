
from Solver import applaySolver

def getPathCSV(csvSelected: int):
  if csvSelected == 1:
    return 'CalculoNumerico/csv/exemplo01.csv'
  elif csvSelected == 2:
    return 'CalculoNumerico/csv/exemplo02.csv'
  elif csvSelected == 3:
    return 'CalculoNumerico/csv/exemplo03.csv'
  elif csvSelected == 4:
    return 'CalculoNumerico/csv/exemplo04.csv'
    
def checkPath(path):
  try:
    file = open(path)
    file.close()
    return True
  except:
    return False

def getCsv(typeInput):
  if typeInput == 2:
    print('Selecione uma das entradas abaixo:')
    print('1 - Exemplo 01')
    print('2 - Exemplo 02')
    print('3 - Exemplo 03')
    print('4 - Exemplo 04')
    
    csvSelect = int(input())
    while csvSelect not in (1,2,3,4):
      print("Entrada não existente. Por favor tente novamente!")
      csvSelect = int(input('Selecione:'))

    pathCSV = getPathCSV(csvSelect)
    return pathCSV
  else:
    pathCSV = input("Digite o caminho do CSV:")
    while checkPath(pathCSV) != True:
      pathCSV = input("Digite o caminho do CSV: ")

    return pathCSV

def selectInput():
  print("Escolha o tipo de entrada:")
  print("1 - Upload do CSV")
  print('2 - CSV Existente no sistema')

  selectInput = int(input())

  while selectInput not in (1,2):
    print('Entrada não reconhecida. Por favor tente novamente!')
    selectInput = int(input("Escolha o tipo de entrada:"))

  return selectInput

def init():
  print('Olá')
  typeInput = selectInput()
  file = getCsv(typeInput)

  applaySolver(file)

init()


