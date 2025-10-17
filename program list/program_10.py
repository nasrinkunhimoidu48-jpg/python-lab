# Read student details from user
student = {}
student["name"] = input("Enter name: ")
student["roll_number"] = input("Enter roll number: ")
student["register_number"] = input("Enter register number: ")
student["department"] = input("Enter department: ")
student["semester"] = int(input("Enter semester: "))

# Add total mark from user
student["total_mark"] = int(input("Enter total mark: "))

# Find grade and add to dictionary
mark = student["total_mark"]
if mark >= 90:
    grade = "A"
elif mark >= 82:
    grade = "B"
elif mark >= 75:
    grade = "C"
elif mark >= 60:
    grade = "D"
elif mark >= 50:
    grade = "P"
else:
    grade = "Fail"
student["grade"] = grade

# Display student details
print(student)


# Delete roll number
del student["roll_number"]

print ("the roll no is deleted and the new dictionary is:\n",student)
