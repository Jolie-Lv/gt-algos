# Dynamic programming approach to find the longest common subsequence.
import sys

def lcs(x, y):
  l = [[0 for y in range(len(y) + 1)] for x in range(len(x) + 1)]
  for i in range(1, len(x) + 1):
    for j in range(1, len(y) + 1):
      # Look in top left diagonal if the letters are equal and add one.
      if x[i - 1] == y[j - 1]:
        l[i][j] = 1 + l[i - 1][j - 1]
      else:
        # Otherwise take the max of the left or top neighbor.
        l[i][j] = max(l[i - 1][j], l[i][j - 1])

  # Return the last element in the matrix.
  return l[len(x)][len(y)], l

def reconstruct_seq(x, y, l):
  # Reconstructs the sequence by traversing from the bottom right to the top
  # left. Indices where all top-left neighbors (top, left, top-left) are 1 less
  # than the current value are subsequence matches and should be recorded.
  s = ''
  v = l[len(x)][len(y)]

  i = len(x)
  j = len(y)
  while v > 0 or i == 0 or j == 0:
    # The target should be 1 less than the current subsequence length.
    t = v - 1
    if l[i - 1][j - 1] == t and l[i - 1][j] == t and l[i][j - 1] == t:
      # If all conditions are satisfied, record the sequence and move upwards.
      s += x[i - 1]
      v -= 1
    elif l[i - 1][j] == v:
      # If the left item is the same value, move one to the left.
      i -= 1
    elif l[i][j - 1] == v:
      # If the top item is the same value, move one to the top.
      j -= 1

  # Return the reversed string.
  return s[::-1]

if __name__ == '__main__':
  x = None
  y = None
  if len(sys.argv) == 3:
    x = sys.argv[1]
    y = sys.argv[2]
  else:
    x = 'BCDBCDA'
    y = 'ABECBAB'

  length, l = lcs(x, y)
  print(length)
  print(reconstruct_seq(x, y, l))

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
