
# def greet(name):
#     print(f"Hello, {name}")
    
# greet("Nothando")

# def add(a, b):
#     return a + b

# result = add(2, 5)
# print(result)

def factorial(n):
    if n == 0:
       return 1
    else:
        return 0*factorial(n-1)
    
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")
    
greet("Noks", "Good Morning")