import os

name = input("Enter the file name (without extension): ")
for file in os.listdir():
    if file.startswith(name + "."):
  
        extension = file.split(".")[-1]
        print("The extension of the file is:", extension)
        break
else:
    print("File not found.")
