def search(list, target):
  for index, value in enumerate(list):
    if value == target:
      return index


arr = [2, 5 ,8, 9, 10, 16, 22]
target = 10

print(search(arr, target))