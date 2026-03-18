# 1).Square Of A Number
def square(num,exp=2):
    return num**exp
print(square(5))
print(square(5,3))
print(square(2,4))

# 2).Default Argument
def greet(name="Guest"):
    print("Hello ",name)
greet("Ram")
greet()

# 3).Default Argument
def add(a,b=4):
    print("Sum = ",a+b)
add(2)
add(2,5)