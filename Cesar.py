def descifrado_Cesar():
  alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
  texto = input("Ingrese el texto para descifrar:")
  rotaciones = 8
  texto_cifrado = ""
  
  for i in texto.upper():
    if i in alfabeto:
      posicion = alfabeto.index(i)
      posicion = (posicion - int(rotaciones))
      posicion % len(alfabeto)
      texto_cifrado + = alfabeto[posicion]
      
    else
       texto_cifrado+ = i
  if 0 < rotaciones < = 27:
    print("Texto cifrado:" + (texto))
    print("Texto descifrado: + (texto_cifrado))
          
descifrado_cesar()
