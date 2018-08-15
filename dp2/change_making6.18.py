# Make change for a given amount without reusing a coin.
# This is the knapsack problem without reuse. The weight is equal to the value,
# and the max-value of the amount needs to equal the change.


def make_change(d, c):
  k = [[0 for x in range(c + 1)] for x in range(len(d) + 1)]

  for i in range(1, len(k)):
    for j in range(1, len(k[0])):
      if d[i - 1] <= j:
        k[i][j] = max(d[i - 1] + k[i - 1][j - d[i - 1]], k[i - 1][j])
      else:
        k[i][j] = k[i - 1][j]
  return k[len(d)][c], k

def reconstruct_change(d, k):
  j = len(k[0]) - 1
  items = []

  for i in range(len(k) - 1, 0, -1):
    if k[i][j] - d[i - 1] == k[i - 1][j - d[i - 1]]:
      # Add the coin if the current value minus the coin's value is equal to
      # the max value without the coin.
      items.append(d[i - 1])
      j -= d[i - 1]
  return items

if __name__ == '__main__':
  d = [5, 12, 25]
  c = 30

  value, k = make_change(d, c)
  if value == c:
    print(reconstruct_change(d, k))
  else:
    print('Cannot construct exact change.')

  top = ''
  for x in range(c + 1):
    top += str(x) + ' ' * (2 - int(x//10 > 0))
  print(top)
  print('-' * len(top))
  for row in k:
    s = ''
    for x in row:
      s += str(x)
      s += ' ' * (2 - int(x//10 > 0))
    print(s)
