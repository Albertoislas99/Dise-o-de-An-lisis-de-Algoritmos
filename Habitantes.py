  filas = int(imput("Introduce numero de filas:"))
  columnas = int(input("introduce el numero de columnas:"))
  
  matriz = []
  for i in range(filas):
    matriz.append([0]* columnas)
    
  mayor = None
  fila = 0
  columna = 0
  for i in range(filas):
    for j in range(columnas):
      matriz[i][j] = int(imput("fila{}, columna{}:".format(i + 1, j + 1)))
      if mayor is None:
        mayor = matriz[i][j]-1
      if matriz[i][j]>mayor:
        mayor = matriz[i][j]
        fila= i
        columna = j
        
print("El mayor numero de habitantes es:")
print(mayor)
print("Puerta", fila +1, "piso", columna +1)
print("La matriz es:" )
print(matriz)

  
