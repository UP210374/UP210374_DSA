A = [34, 50, 32, 9, 90, 43]
length = len(A)
i = 0
#loop para recorrer la matriz
while i < length:
      j = i
      #loop para realizar las comparaciones
      while j < length:
              if A[i] > A[j]:
                      aux = A[i]
                      A[i] = A[j]
                      A[j] = aux
              j += 1
      i += 1

print("Lista ordenada: ")
print(A)