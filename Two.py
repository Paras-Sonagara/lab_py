try:
    my_list = [1, 2, 3]
    print(my_list[1])
    
except IndexError:
    print("Index is out of range!")
else:
    print("Element found successfully!")
finally:
    print("Program finished.")
