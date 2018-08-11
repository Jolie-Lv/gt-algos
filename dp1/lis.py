# Dynamic programming approach to find the longest increasing subsequence.
import sys

def lis(sequence):
  l = [0] * len(sequence)
  for i in range(0, len(sequence)):
    # Assume the longest increasing subsequence at i is 1.
    l[i] = 1

    # Get the maximum L value for the previous j indices. The goal is to find
    # a smaller sequence value that has the largest LIS value.
    for j in range(0, i):
      # The sequence value must be smaller than the current value (hence
      # increasing), and the LIS must be longer than the current value.
      if sequence[j] < sequence[i] and l[i] < 1 + l[j]:
        l[i] = 1 + l[j]
  return max(l), l

def recover_sequence(sequence, inc, length):
  s = []
  curr_length = length
  # Iterate backwards through the LIS list. Start with the highest value and
  # continually decrement to get the LIS.
  for i in range(len(inc) - 1, -1, -1):
    if inc[i] == curr_length:
      s.append(sequence[i])
      curr_length -= 1

    if curr_length <= 0:
      break

  s.reverse()
  return s

if __name__ == '__main__':
  sequence = []
  if len(sys.argv) > 1:
    sequence = map(lambda x: int(x), sys.argv[1:])
  else:
    sequence = [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9]

  length, inc = lis(sequence)
  print(length)
  print(recover_sequence(sequence, inc, length))
