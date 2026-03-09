from array import array

#1.
arr = array('i', [10,20,30,40,50])
print(len(arr))

#2.
arr = array('i', [10,20,30])
arr.append(40)
print(arr)

#3.
arr = array('i', [10,20,40])
arr.insert(2,30)
print(arr)

#4.
arr = array('i', [10,20,30,40])
arr.remove(20)
print(arr)

#5.
arr = array('i', [10,20,30,40])
x=arr.pop()
print("Removed :",x)
print(arr)

#6.
arr = array('i', [10,20,30,40])
print(arr.index(30))

#7.
arr = array('i', [10,20,30,20,40,20])
print(arr.count(20))

#8.
arr = array('i', [10,20,30,40])
arr.reverse()
print(arr)