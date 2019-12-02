import heapq

lista = [43, 36, 25, 89, 13, 23, 34]

suma = 0

for i in lista:
  suma += i

heapq.heapify(lista)

print(suma)
print(heapq.heappop(lista))