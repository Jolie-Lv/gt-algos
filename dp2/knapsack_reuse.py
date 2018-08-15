# Knapsack problem that allows for reuse of items. Problem is also solved in
# O(nB) time, but is not polynomial.

def knapsack(w, v, B):
  k = [0] * (B + 1)
  s = [0] * (B + 1)

  for b in range(1, len(k)):
    k[b] = 0
    s[b] = 0
    for i in range(len(w)):
      # Look through all of the potential items.
      if w[i] <= b and k[b] < v[i] + k[b - w[i]]:
        # Find the item that can fit, and that will maximize the current value.
        # Append what index was used to increase the value of the item.
        k[b] = v[i] + k[b - w[i]]
        s[b] = i
  return k[B], k, s

def reconstruct_knapsack(w, v, k, s):
  i = len(k) - 1
  items = []

  while i > 0:
    idx = s[i]
    items.append((w[idx], v[idx]))
    i -= w[idx]

  return items

if __name__ == '__main__':
  weights = [12, 15, 10, 5]
  values =  [10, 8, 8, 1]
  b = 34

  v, k, s = knapsack(weights, values, b)
  print(v)
  print(reconstruct_knapsack(weights, values, k, s))

  # Pretty print of k.
  top = ''
  for x in range(b + 1):
    top += str(x) + ' ' * (2 - int(x//10 > 0))
  print(top)
  print('-' * len(top))

  st = ''
  for x in k:
    st += str(x)
    st += ' ' * (2 - int(x//10 > 0))
  print(st)

  # Pretty print of what index was selected.
  idxs = ''
  for x in s:
    idxs += str(x)
    idxs += ' ' * (2 - int(x//10 > 0))
  print(idxs)
