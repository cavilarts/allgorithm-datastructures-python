
""" 
  ***** BETTER *****
  Iterative approach
  calculate_factorial
  @params n = int
  @return int
"""
def calculate_factorial(n: int) -> int:
  total = 1

  for i in range(2, n + 1):
    total *= i

  return total
""" 
  Recursive approach
  calc_factorial
  @params n = int
  @return int
"""
def calc_factorial(n: int) -> int:
  if n == 1:
    return n
  
  return n * calc_factorial(n - 1)


print(calc_factorial(6))
print(calculate_factorial(6))