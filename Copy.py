src = open("CC.txt", "r")
data = src.read()
src.close()

dst = open("CV.txt", "w")
dst.write(data)
dst.close()
print("File copied successfully.")