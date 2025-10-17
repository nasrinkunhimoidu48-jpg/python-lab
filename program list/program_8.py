print("String occurrence replace with $")
stri=(input("Enter the string: "))
first_char = stri[0]
result = first_char + stri[1:].replace(first_char, '$')
print(result)
