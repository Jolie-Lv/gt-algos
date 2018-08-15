# Chain multiplication. Finds optimal way to multiply a set of matrices.

def chain_multiply(m):
  # Diagonals are 0.
  c = [[0 for x in range(len(m))] for x in range(len(m))]
  # S keeps track of what was the partition index used for each iteration.
  S = [[0 for x in range(len(m))] for x in range(len(m))]

  for s in range(1, len(m)):
    # s is the offset from the diagonal. This moves from the diagonal to the
    # upper right corner.
    for i in range(1, len(m) - s):

      # i is the column in the matrix.
      # j is the row in the matrix.
      j = i + s
      c[i][j] = float('inf')
      for l in range(i, j):
        # m[i - 1] * m[l] * m[j] is the number of operations needed to compute
        # that matrix. c[i][l] computes the prefix, c[l + 1][j] computes the
        # suffix.
        # If the total number of operations required is less than the current
        # min, replace the value.
        curr = m[i - 1] * m[l] * m[j] + c[i][l] + c[l + 1][j]
        if c[i][j] > curr:
          c[i][j] = curr
          S[i][j] = l

  # The min cost is the top right value in the matrix. Also return the cost
  # matrix and the parition matrix.
  return c[1][len(m) - 1], c, S

def print_cost(c, m):
  # Neatly prints the cost matrix with the target values.
  st = ' ' * 6
  for i in m:
    st += str(i) + ' ' * (6 - len(str(i)))
  print(st)
  print('-' * len(st))

  for idx, row in enumerate(c):
    s = str(m[idx]) + ' ' * (5 - len(str(m[idx]))) + '|'
    for x in row:
      s += str(x)
      s += ' ' * (6 - len(str(x)))
    print(s)

def reconstruct_chain(m, S, i , j):
  if i < j:
    # Recursively get the prefix and suffix for a given chain.
    x = reconstruct_chain(m, S, i, S[i][j])
    y = reconstruct_chain(m, S, S[i][j] + 1, j)
    # "Fake multiply" them together by returning a formatted string of the mult.
    return '(' + str(x) + ' * ' + str(y) + ')'
  else:
    return str(m[i - 1]) + 'x' + str(m[i])

if __name__ == '__main__':
  # Matrix size is M-1xM. Start from index 1.
  # 50x20, 20x10, 10x35, 35x5.
  matrices = [20, 35, 10, 5, 15, 50]
  cost, c, S = chain_multiply(matrices)

  print(cost)
  print(reconstruct_chain(matrices, S, 1, len(c) - 1))

  print('\nCost Matrix')
  print_cost(c, matrices)
  print('\nSelected Index Matrix')
  print_cost(S, matrices)
