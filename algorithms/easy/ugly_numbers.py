def nth_ugly(n):
  dpUgly = [1]  
  u2 = u3 = u5 = 0
  multiple_2 = 2
  multiple_3 = 3
  multiple_5 = 5
  
  for i in range(1, n):
    next_ugly = min(multiple_2, multiple_3, multiple_5)
    dpUgly.append(next_ugly)
    
    if next_ugly == multiple_2:
      u2 += 1
      multiple_2 = dpUgly[u2] * 2
      
    if next_ugly == multiple_3:
      u3 += 1
      multiple_3 = dpUgly[u3] * 3
      
    if next_ugly == multiple_5:
      u5 += 1
      multiple_5 = dpUgly[u5] * 5
      
  return dpUgly[- 1]

n = 15
print(f"{n}th ugly number is: {nth_ugly(n)}")
      