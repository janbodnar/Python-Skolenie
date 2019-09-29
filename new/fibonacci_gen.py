# fibonacci_gen.py


def fib():
    
   a, b = 0, 1

   while True:
      yield b
      
      a, b = b, a + b


g = fib()

try:

   for e in g:
      print(e)
            
except KeyboardInterrupt:
   print("Calculation stopped")
