# Knapsack problem with no repitition. Problem is solved in O(nB) time, but is
# non-polynomial.
import sys

def knapsack(w, v, B):
  # Initialize k to have zero weights everywhere. Should include an empty col
  # and row for "0".
  k = [[0 for x in range(B + 1)] for x in range(len(w) + 1)]

  for i in range(1, len(w) + 1):
    for b in range(1, B + 1):
      if w[i - 1] <= b:
        # Calculate the greater value by either taking the current piece or
        # leaving it.
        k[i][b] = max(v[i - 1] + k[i - 1][b - w[i - 1]], k[i - 1][b])
      else:
        # Items that won't fit cannot be added.
        k[i][b] = k[i - 1][b]

  # Return bottom right item.
  return k[len(w)][B], k

def reconstruct_knapsack(w, v, k, value):
  j = len(k[0]) - 1

  items = []
  for i in range(len(k) - 1, -1, -1):
    # Add the item if the value-difference between one item and the next is
    # equal to the item's value.
    if k[i][j] - k[i - 1][j - w[i - 1]] == v[i - 1]:
      items.append((w[i - 1], v[i - 1]))
      j -= w[i - 1]
    i -= 1
  return items

if __name__ == '__main__':
  weights = [15, 12, 10, 5]
  values =  [15, 10, 8, 1]
  b = 22

  v, k = knapsack(weights, values, b)
  print(v)
  print(reconstruct_knapsack(weights, values, k, v))

  # Pretty print of k.
  top = ''
  for x in range(b + 1):
    top += str(x) + ' ' * (2 - int(x//10 > 0))
  print(top)
  print('-' * len(top))
  for row in k:
    s = ''
    for x in row:
      s += str(x)
      s += ' ' * (2 - int(x//10 > 0))
    print(s)
