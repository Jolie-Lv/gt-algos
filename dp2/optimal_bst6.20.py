# Create an optimal Binary Search Tree (BST) for an alphabetical list of words.
# Words have associated probability values, and the BST should be optimized such
# that the expected number of comparisons is minizmized.

def optimal_bst(p):
  # Cost of the BST.
  c = [[0 for x in range(len(p))] for x in range(len(p))]
  # The partition index for each subtree.
  S = [[0 for x in range(len(p))] for x in range(len(p))]
  # The cumulative probabilities thus far.
  w = [[0 for x in range(len(p))] for x in range(len(p))]

  for i in range(len(p)):
    c[i][i] = p[i]
    S[i][i] = i
    w[i][i] = p[i]

  for s in range(1, len(c)):
    for i in range(len(c) - s):
      j = i + s
      c[i][j] = float('inf')
      w[i][j] = w[i][j - 1] + p[j]
      # Important! Look at all items in the range [i...j].
      for l in range(i, j + 1):
        # Some ranges might go out of bounds, so make sure that they are guarded
        # by adding zero if they do.
        # Make sure that looking one index to the left of a potential root is
        # still in bounds. Likewise, looking one index to the right. Looking
        # out of bounds means that that subtree will have a cost of 0 (empty).
        # Cost = left subtree + right subtree + sum of p[i...j].
        # sum(p[i...j]) Is the probability that an query passes through this new
        # subtree.
        cost = (
          (c[i][l - 1] if l > 0 else 0) +
          (c[l + 1][j] if l < len(c) - 1 else 0) +
          w[i][j]
        )

        # Set the current minimum and root used for that index.
        if cost < c[i][j]:
          c[i][j] = cost
          S[i][j] = l

  return c[0][-1], c, S

def reconstruct_bst(bst, depth_arr, d, i, j):
  if i < j:
    # Assign the depth to be min depth seen.
    depth[bst[i][j]] = min(depth[bst[i][j]], d)

    # Reconstruct left and right subtrees.
    reconstruct_bst(bst, depth, d + 1, i, bst[i][j] - 1)
    reconstruct_bst(bst, depth, d + 1, bst[i][j] + 1, j)
  else:
    depth[j] = d

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
      x_str = str(round(x, 2))
      s += x_str
      s += ' ' * (6 - len(x_str))
    print(s)

if __name__ == '__main__':
  words = ['begin', 'do', 'else', 'end', 'if', 'then', 'while']
  probs = [5,    40,  8,   4,  10,  10,     23]
  # probs = [0.25, 0.2, 0.05, 0.2, 0.3]
  # probs = [1, 2, 4, 3]

  cost, c, s = optimal_bst(probs)
  print(cost)
  print_cost(c, probs)
  print('\n')
  print_cost(s, probs)

  depth = [float('inf')] * len(words)
  reconstruct_bst(s, depth, 1, 0, len(words) - 1)
  print(depth)

  #optimal:
  #      /  do  \                   0.4
  # begin    / while        0.05          0.23
  #        / if \                       0.1
  #     else \   then                0.08   0.1
  #         end                         0.04

  # 1 * 0.4 + 2 * (0.05 + 0.23) + 3 * (0.1) + 4 * (0.08 + 0.1) + 5 * (0.04) = 2.18
