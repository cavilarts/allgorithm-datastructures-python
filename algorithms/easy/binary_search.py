def binary_search(list, target):
  mid = len(list) // 2
  
  if list[mid] == target: 
    return "Found"
  elif list[mid] > target:
    return binary_search(list[:mid], target)
  else:
    return binary_search(list[mid:], target)
  

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))


def binary_search_iterative(list, target):
  start, end, = 0, len(list) -1

  while start <= end:
    mid = (start + end) // 2
    
    if list[mid] == target:
      return mid
    elif list[mid] < target:
      start = mid + 1
    elif list > target:
      end = mid - 1
  
  return -1

arr = [2, 5, 8, 10, 16, 22, 25]
target = 22
result = binary_search_iterative(arr, target)
print(result)