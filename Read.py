#1.Read
f = open("one.txt", "r")
data = f.read()
print("File Content :",data)
f.close()

#2.Read Specific Number Of Text
f = open("one.txt", "r")
data = f.read(10)
print("File Content :",data)
f.close()

#3.Read One Lines
f = open("one.txt", "r")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print("Line 1 :",line1)
print("Line 2 :",line2)
print("Line 3 :",line3)
f.close()

#4.Read All Lines And Length
f = open("one.txt", "r")
lines = f.readlines()
print("List Of Lines",lines)
print("Number Of Lines",len(lines))
f.close()

#5.Read Specific Lines
f = open("one.txt", "r")
lines = f.readlines()
print(lines[2].strip())
f.close()