# Can you make change using a set of denominations? You can use each coin more
# than once.
# This problem is identical to the knapsack problem with reuse. The weight is
# equal to the value, and you need to verify that the max value is equal to the
# change that needs to be made.

def make_change(d, c):
  b = [0] * (c + 1)
  s = [0] * (c + 1)

  for i in range(1, len(b)):
    b[i] = 0
    for j in range(len(d)):
      if d[j] <= i and b[i] <= d[j] + b[i - d[j]]:
        b[i] = d[j] + b[i - d[j]]
        s[i] = j

  return b[c], b, s

def reconstruct_change(v, s, d):
  c = []
  i = len(s) - 1

  while i > 0:
    c.append(d[s[i]])
    i -= d[s[i]]
  return c

if __name__ == '__main__':
  d = [5, 12, 25]
  c = 20

  value, v, s = make_change(d, c)
  if value == c:
    print(reconstruct_change(v, s, d))
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
