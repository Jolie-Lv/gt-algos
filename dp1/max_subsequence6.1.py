# Gets the maximum value for a substring in an array.
import sys

def max_substring(s):
  l = [0] * len(s)
  l[0] = s[0]
  for i in range(1, len(s)):
    # Take the greater of the current sequence value or the total until then.
    l[i] = max(s[i] + l[i - 1], s[i])
  return max(l), l

def recover_sequence(s, l, total):
  # Get the ending index (aka the max value) from the total array.
  end_idx = l.index(total) + 1
  start_idx = end_idx

  # Work backwards through the array until the total array's value matches the
  # sequences value. This siginifies a starting point.
  while s[start_idx] != l[start_idx]:
    start_idx -= 1

  # Return the subarray.
  return s[start_idx:end_idx]

if __name__ == '__main__':
  sequence = []
  if len(sys.argv) > 1:
    sequence = map(lambda x: int(x), sys.argv[1:])
  else:
    sequence = [5, 7, 4, -3, -9, -5, 10, 4, 5, 8, 9, -7]

  total, l = max_substring(sequence)
  print(total)
  print(recover_sequence(sequence, l, total))
