#1.Basic Positional Arguments
def add(a,b):
    print("a =",a)
    print("b =",b)
    return a+b
result=add(2,5)
print("Sum =",result)

#2.Student Information
def Student_info(name,roll,marks):
    print("Name :",name)
    print("Roll No :",roll)
    print("Marks :",marks)
Student_info("Ravi",101,85)

#3.Simple Interest
def Simple_interest(p,r,n):
    si=(p*r*n)/100
    print("Simple Interest :",si)
Simple_interest(10000,2,2)
Simple_interest(50000,1.2,3)

#4.Area Of Circle 
def ar_circle(r):
    a_circle=3.14*r*r
    print("Area Of Circle :",a_circle)
ar_circle(1.5)
ar_circle(4)

#5.Check Number Positive Negative Or Zero
def check_value(no):
    if (no>0):
        print("Positive")
    elif (no<0):
        print("Negative")
    else:
        print("Zero")
check_value(0)
check_value(90)
check_value(-15)
        
#6.Odd Or Even
def odd_even(no):
    if (no%2==0):
        print(f"Value {no} Is Even")
    else:
        print(f"Value {no} Is Odd")
odd_even(50)
odd_even(15)

#7.Arithmatic Operation Substraction,Multiplication And Division
def arithmatic_operation(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    print("Addition Of Two Value Is :",add)
    print("Substraction Of Two Value Is :",sub)
    print("Multiplication Of Two Value Is :",mul)
    print("Division Of Two Value Is :",div)
arithmatic_operation(50,10.5)
arithmatic_operation(100,200)