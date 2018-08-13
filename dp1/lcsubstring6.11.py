# Gets the longest common substring. The strings must be continuous.
import sys

def lcs(x, y):
  l = [[0 for y in range(len(y) + 1)] for x in range(len(x) + 1)]
  max_l = 0
  for i in range(1, len(x) + 1):
    for j in range(1, len(y) + 1):
      # Look in top left diagonal if the letters are equal and add one.
      if x[i - 1] == y[j - 1]:
        l[i][j] = 1 + l[i - 1][j - 1]
        max_l = max(l[i][j], max_l)
      else:
        # Otherwise take the max of the left or top neighbor.
        l[i][j] = 0

  # Return the last element in the matrix.
  return max_l, l

def reconstruct_seq(x, y, l, max_l):
  s = ''
  idx = 0

  max_val = 0
  for i in range(len(l)):
    row_max = max(l[i])
    if row_max > max_val:
      max_val = row_max
      idx = i

  return x[idx - max_l: idx]

if __name__ == '__main__':
  x = None
  y = None
  if len(sys.argv) == 3:
    x = sys.argv[1]
    y = sys.argv[2]
  else:
    x = 'ABCDEABC'
    y = 'ABCFABCD'

  length, l = lcs(x, y)
  print(length)
  print(reconstruct_seq(x, y, l, length))

  top = '_ _ '
  for letter in y:
    top += letter + ' '
  print(top)

  for idx, row in enumerate(l):
    s = '_ '
    if idx > 0:
      s = x[idx - 1] + ' '

    for item in row:
      s += str(item) + ' '
    print(s)
