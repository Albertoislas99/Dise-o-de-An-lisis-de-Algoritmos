def bucketSort(arreglo):
    cubeta = []
    
    for i in range(len(arreglo)):
        cubeta.append([])
        
    for j in arreglo:
        index_b = int(10 * j)
        cubeta[index_b].append(j)
        
    for i in range(len(arreglo)):
        cubeta[i] = sorted(cubeta[i])
        
    k = 0
    for i in range(len(arreglo)):
        for j in range(len(cubeta[i])):
            arreglo[k] = cubeta[i][j]
            k += 1
    return arreglo    
    
arreglo = [.70, .12, .11, .78, .40, .33, .31, .37, .10, .41, .22, .89, .97, .88, .13, .10]
print("El arreglo ordenado queda de la siguiente manera:")
print(bucketSort(arreglo))
 
