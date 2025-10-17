def read_number():
    num = input("Enter a number (min 4 digits): ")
    return num

def reverse_number(num):
    return num[::-1]

num = read_number()
if len(num) >= 4 and num.isdigit():
    print("Original number:", num)
    print("Reversed number:", reverse_number(num))
else:
    print("Invalid input!")
