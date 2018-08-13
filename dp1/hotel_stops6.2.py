# The goal is to pick hotels that are ~200 miles apart from each other as to
# minimize the total error. Error is determined as (200 - h)^2.
import sys
import math

def choose_stops(s):
  l = [0] * len(s)
  for i in range(len(s)):
    # The initial error is the error assuming you make no stops until the hotel.
    l[i] = (200 - s[i]) ** 2
    for j in range(0, i):
      # Find the minimum error thus far. Pick the hotel that minimizes the error
      # for the current stop. This can be stopping at no hotels, or picking an
      # earlier one.
      l[i] = min(l[i], l[j] + (200 - (s[i] - s[j])) ** 2)
  return l[-1], l

def recover_sequence(s, l, error):
  hotels = [s[-1]]
  last_idx = len(s) - 1

  # Iterate backwards through the error list.
  for i in range(len(s) - 2, -1, -1):
    if l[i] > l[last_idx]:
      continue

    # A hotel should be chosen if the error of choosing that hotel matches the
    # calculated error.
    diff = (200 - (s[last_idx] - s[i])) ** 2
    if diff == l[last_idx] - l[i]:
      hotels.append(s[i])
      last_idx = i

  return hotels[::-1]


if __name__ == '__main__':
  sequence = []
  if len(sys.argv) > 1:
    sequence = map(lambda x: int(x), sys.argv[1:])
  else:
    sequence = [50, 175, 240, 385, 425, 560]

  error, l = choose_stops(sequence)
  print(error)
  print(recover_sequence(sequence, l, error))
