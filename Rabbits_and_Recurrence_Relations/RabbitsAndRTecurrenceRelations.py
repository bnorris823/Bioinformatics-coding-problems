def rabbits(n, k):
  if n is 0 or n is 1:
    return 1
  else:
    return (rabbits(n - 1, k) + k * rabbits(n - 2, k))

x = 5
y = 3

    
print(rabbits(x - 1, y))
