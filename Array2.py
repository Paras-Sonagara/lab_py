from array import array

#1.Positive Index
arr=array('i',[10,20,30,40,50])
print(arr[0])
print(arr[2])
print(arr[4])

#2.Negative Index
arr=array('i',[10,20,30,40,50])
print(arr[-1])
print(arr[-3])
print(arr[-5])

#3.Modify Array
arr=array('i',[10,20,30,40,50])
arr[2]=35
print(arr)