def fib(n):
   c = 0

   a = 0
   b = 1
   t = 0
 
   while c <= n:
      print(a)
      t = a + b
      a = b
      b = t
      c = c + 1

# Driver Code
fib(12)
