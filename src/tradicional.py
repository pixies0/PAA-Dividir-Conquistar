lista = [6, 4, 8, 90, 12, 56, 7, 1, 63]

maior = 0
menor = 0

for n in range(len(lista)):
    
    if n == 0:
          maior = menor = lista[n]
    else:
        if lista[n] > maior:
            maior = lista[n]
        if lista[n] < menor:
             menor = lista[n]

print("Maior valor:", maior)
print("Menor Valor:", menor)