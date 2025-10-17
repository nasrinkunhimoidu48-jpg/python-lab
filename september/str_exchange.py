print("String characters exchange")
s = input("Enter the string: ")
if len(s) < 2:
    print("String is too short to exchange characters.")
else:
    new_str = s[-1] + s[1:-1] + s[0]
    print("Result:", new_str)
