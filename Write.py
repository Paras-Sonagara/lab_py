#1.Write A Single String
f = open("one.txt", "w")
f.write("Hello Student \n")
f.write("Welcome To Python Code \n")
f.write("Thank You For Visiting \n")
f.close()

#2.Old Content Is Removed And Add New Content
f = open("one.txt", "w")
f.write("Atmiya University\n")
f.close()

#3.Append(ADD) Line
f = open("one.txt", "a")
f.write("This Content Add At The End\n")
f.close()

#4.Write Multiple Lines
f = open("one.txt", "w")
lines = ["Python Programming\n","File Handling\n","Error Handling\n","Exception Handling\n"]
f.writelines(lines)
f.close()