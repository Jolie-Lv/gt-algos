# Make change with unlimited coins, but you can only use N total coins. This
# is identical to the knapsack problem with reuse, but it limits the number of
# total coins that can be used.

def make_change(d, c):
  # It is important to sort highest to lowest. This way the larger of divisible
  # coins (ex. 10, 5) is always chosen over the smaller value.
  d = sorted(d, reverse=True)
  k = [0] * (c + 1)
  s = [0] * (c + 1)

  for b in range(1, len(k)):
    for i in range(len(d)):
      if d[i] <= b and k[b] < d[i] + k[b - d[i]]:
        k[b] = d[i] + k[b - d[i]]
        s[b] = i
  return k[c], k, s

def reconstruct_change(v, s, d):
  d = sorted(d, reverse=True)
  i = v[-1]
  items = []

  while i > 0:
    items.append(d[s[i]])
    i -= d[s[i]]

  return items

if __name__ == '__main__':
  d = [5, 25, 10]
  c = 35
  k = 4

  value, v, s = make_change(d, c)
  if value == c:
    coins = reconstruct_change(v, s, d)
    if len(coins) <= k:
      print(coins)
    else:
      print('Cannot make exact change with limited coins.')
  else:
    print('Cannot construct exact change.')

  # Pretty print of k.
  top = ''
  for x in range(c + 1):
    top += str(x) + ' ' * (2 - int(x//10 > 0))
  print(top)
  print('-' * len(top))

  st = ''
  for x in v:
    st += str(x)
    st += ' ' * (2 - int(x//10 > 0))
  print(st)

  # Pretty print of what index was selected.
  idxs = ''
  for x in s:
    idxs += str(x)
    idxs += ' ' * (2 - int(x//10 > 0))
  print(idxs)
