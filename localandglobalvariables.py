x = 10 # Global variable

def my_function():
  x = 5 # Local variable
  print("Local x:", x)

my_function() # Prints the local x
print("Global x:", x)