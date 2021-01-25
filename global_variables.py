# Global variable inside a function

def myfunc():
  global x
  x = "is a programming language"

myfunc()

print("Python is " + x) 

# Global variable outside a function
x = "kind of fun."

def myfunc():
  print("programing is " + x)

myfunc() 