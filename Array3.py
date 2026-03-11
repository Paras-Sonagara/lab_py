from array import array

#1.Basic Slice
arr=array('i',[10,20,30,40,50,60,70])
print(arr[1:4])
print(arr[1:3])
print(arr[3:])
print(arr[:])

#2.Slicing With Step
arr=array('i',[10,20,30,40,50,60,70])
print(arr[::2])
print(arr[1::2])
print(arr[::3])

#3.Negative Slicing
arr=array('i',[10,20,30,40,50])
print(arr[-4:-1])
print(arr[-3:])
print(arr[:-2])

#4.Reverse Array Using Slicing
arr=array('i',[10,20,30,40,50])
print(arr[::-1])

#4.Modifying Slice
arr=array('i',[10,20,30,40,50])
arr[1:4]=array('i',[25,35,45])
print(arr)