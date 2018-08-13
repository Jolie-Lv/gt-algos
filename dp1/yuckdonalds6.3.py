# You are given an array of estimated profits for a location as well as their
# mile markers. The goal is to find the chain of locations that maximize profit
# as long as they are k-miles apart from each other.
import sys

def profit_seeker(miles, profits, k):
  l = [0] * len(miles)
  for i in range(len(miles)):
    # Initial profit is the profit of that location.
    l[i] = profits[i]
    for j in range(i - 1, -1, -1):
      # Iterate backwards from the current location and look for a location that
      # is more than k-miles away and has greater total profits than any other
      # chain of locations.
      if miles[i] - miles[j] >= k and profits[i] + l[j] > l[i]:
        l[i] = profits[i] + l[j]
  return max(l), l

def recover_sequence(miles, profits, l, p):
  s = []
  curr_p = p
  for i in range(len(l) - 1, -1, -1):
    # Iterate backwards through the array and look for indices where the current
    # profit matches the total.
    if l[i] == curr_p:
      curr_p -= profits[i]
      s.append((miles[i], profits[i]))

  return s[::-1]

if __name__ == '__main__':
  miles = [20, 25, 35, 40, 55, 60, 75]
  profits = [7, 5, 8, 3, 20, 10, 6]
  k = 15

  p, l = profit_seeker(miles, profits, k)
  print(p)
  print(recover_sequence(miles, profits, l, p))
