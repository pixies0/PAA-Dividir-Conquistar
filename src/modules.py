# EXEMPLO - ENCONTRE O MENOR E O MAIOR ELEMENTO EM UMA MATRIZ

# Neste problema, recebemos uma matriz de elementos e temos que encontrar o 
# elemento mínimo e máximo da matriz fornecida. Resolveremos o problema dado pelo 
# algoritmo de dividir e conquistar. Aqui, dividimos os elementos como a primeira etapa
# do algoritmo de divisão e conquista, encontramos os elementos mínimos e máximos da 
# matriz como conquista da solução e finalizamos a resposta no final combinando os resultados.

def divideAndConquer_Max(arr, ind, len):

    maximum = -1 # Será atualizada com o valor máximo encontrado.

    if (ind >= len - 2): #Debugar aqui
        if (arr[ind] > arr[ind + 1]):
            return arr[ind]
        else:
            return arr[ind + 1]
        
    maximum = divideAndConquer_Max(arr, ind + 1, len) #Debugar aqui

    if(arr[ind] > maximum): #Debugar aqui
        return arr[ind]
    else:
        return maximum
    
def divideAndConquer_Min(arr, ind, len):

    minimum = 0
    if (ind >= len - 2):
        if (arr[ind] < arr[ind + 1]):
            return arr[ind]
        else:
            return arr[ind + 1]
        
    minimum = divideAndConquer_Min(arr, ind + 1, len)

    if(arr[ind] < minimum):
        return arr[ind]
    else:
        return minimum
    


 