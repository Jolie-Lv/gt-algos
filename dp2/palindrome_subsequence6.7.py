# Given a string, find the longest palindrome subsequence.

def longest_palindrome(seq):
  l = [[0 for x in range(len(seq))] for x in range(len(seq))]
  w = [[0 for x in range(len(seq))] for x in range(len(seq))]

  for i in range(0, len(l)):
    l[i][i] = 1

  for s in range(1, len(l)):
    for i in range(len(l) - s):
      j = i + s

      if seq[i] == seq[j]:
        if j - i == 1:
          l[i][j] = 2
        else:
          l[i][j] = 2 + l[i + 1][j - 1]
      else:
        l[i][j] = max(l[i + 1][j], l[i][j - 1])

  return l[0][-1], l

def print_l(l, seq):
  top = '  '
  for letter in seq:
    top += letter + ' '
  print(top)

  for idx, row in enumerate(l):
    s = seq[idx] + ' '
    for item in row:
      s += str(item) + ' '
    print(s)

def reconstruct_seq(seq, l):
  i = 0
  j = len(l) - 1

  p = ''

  while i <= j:
    if seq[i] == seq[j]:
      p += seq[i]
      i += 1
      j -= 1
    elif l[i][j - 1] > l[i + 1][j]:
      j -= 1
    else:
      i += 1

  if l[0][len(l) - 1] % 2 == 0:
    p += p[::-1]
  else:
    p += p[:1:-1]

  if len(p) == 0:
    p = l[-1]

  return p


if __name__ == '__main__':
  seq = 'ACGTGTCAAAATCG'

  length, l = longest_palindrome(seq)
  print(length)
  print(reconstruct_seq(seq, l))
  print_l(l, seq)
