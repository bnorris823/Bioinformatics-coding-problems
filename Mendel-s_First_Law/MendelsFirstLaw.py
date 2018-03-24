def first_law(k, m, n):
  
  N = k + m + n
  return 1 - (m*n + 0.25*m*(m-1) + n*(n-1)) / (N*(N - 1))
  
print(first_law(22, 17, 29))  
