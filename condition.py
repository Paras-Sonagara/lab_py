age = int(input("Enter Your Age :"))
if age >= 18:
    print("You Are Eligible")
else:
    print("You Are Not Eligible")
    
mark = int(input("\nEnter Your Marks :"))
if mark >= 90:
    print("\tYou Will Get A Grade")
elif mark >=75:
    print("\tYou Will Get B Grade")
elif mark >=40:
    print("\tYou Will Get C Grade")
else:
    print("\tYou Fail In Exam")
