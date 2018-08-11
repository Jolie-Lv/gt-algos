# Dynamic programming approach to a fibonacci number.
import sys

def main(fib):
  f = [0] * (fib + 1)
  f[1] = 1

  for i in range(2, fib):
    f[i] = f[i - 1] + f[i - 2]

  print(f[fib - 1])


if __name__ == '__main__':
  if len(sys.argv) == 2:
    main(int(sys.argv[1]) + 1)
