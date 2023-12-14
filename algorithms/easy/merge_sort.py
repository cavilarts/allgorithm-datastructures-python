def merge_sort(array):
  if len(array) <= 1:
    return array

  middle = len(array) // 2
  left = merge_sort(array[:middle])
  right = merge_sort(array[middle:])

  return merge(left, right)

def merge(left, right):
  result = []
  left_index = right_index = 0

  while left_index < len(left) and right_index < len(right):
    if left[left_index] <= right[right_index]:
      result.append(left[left_index])
      left_index += 1

    else:
      result.append(right[right_index])
      right_index += 1

  if left:
    result.extend(left[left_index:])

  if right:
    result.extend(right[right_index:])

  return result
  
print(merge_sort([10, 4, 8, 5, 2, 6, 1, 7, 3, 9]))