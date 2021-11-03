import numpy as np
from ortools.linear_solver import pywraplp

def applaySolver(file: str):
  readerCsv=np.loadtxt(file,
                  delimiter=',',
                  unpack=False,
                  dtype='int'
                )

  solver = pywraplp.Solver.CreateSolver('GLOP')
  variaveis = []

  def solveEquation(lineEquation: np.array):
    valorFinal = lineEquation[-1]
    rangeValue = len(lineEquation) - 1
    if(len(variaveis) <= 0):
      for i, _ in enumerate(range(rangeValue)):
        variaveis.append(solver.NumVar(-solver.infinity(), solver.infinity(), 'x'+str(i)))
    
    createSistem = 0

    for i, _ in enumerate(range(rangeValue)):
      createSistem += lineEquation[i]*variaveis[i]
    
    solver.Add(createSistem == valorFinal) 

  for lineFile in readerCsv:
    solveEquation(lineFile)

  status = solver.Solve()

  if(status > 1):
    print('Sistema sem solução')
  else:
    for i, _ in enumerate(range(len(variaveis))):
      print(f'O valor de x{i+1} e {variaveis[i].solution_value()}' )