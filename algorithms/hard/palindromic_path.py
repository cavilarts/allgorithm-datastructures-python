def is_palindrome(string):
  if string == string[::-1]:
    return True
  else:
    return False
  
def palindromic_path(string, a, i, j, m , n):
  if j < m - 1 or  i < n - 1:
    if i < n - 1:
      palindromic_path(string + a[i][j], a, i + 1, j, m, n)
    if j < m -1:
      palindromic_path(string + a[i][j], a, i, j + 1, m, n)
  else:
    string = string + a[n - 1][m - 1]
    if is_palindrome(string):
      print(string)
      
a = [['a', 'a', 'a'],
     ['b', 'b', 'a'],
     ['a', 'b', 'a']]

str = ""
print(palindromic_path(str, a, 0, 0, 3, 3))