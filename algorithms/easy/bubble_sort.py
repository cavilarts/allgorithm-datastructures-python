def bubble_sort(list):
  iterations = 0
  
  for i in range(len(list)):
    for j in range(len(list) - i - 1):
      iterations += 1
      if list[j] > list[j + 1]:
        list[j], list[j + 1] = list[j + 1], list[j]
  
  return list, iterations

A = [9, 8, 7, 6, 5, 4, 3, 2 ,1]
print(bubble_sort(A))