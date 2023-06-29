from modules import *

minimum, maximum = 0, -1

arr = [6, 4, 8, 90, 12, 56, 7, 1, 63]

# arr = [6, 4, 8, 90, 12, 63, 7, 1, 56]


maximum = divideAndConquer_Max(arr, 0, 9)
minimum = divideAndConquer_Min(arr, 0, 9)

print("O maior valor é: ", maximum) 
print("O menor valor é: ", minimum)
