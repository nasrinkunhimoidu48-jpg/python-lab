print("\nmenu")
print("options\n1= occurrence of word\n2=character frequency\n3=display the factors of given number\n4=exit ")
while True:
    
    
    option = input("enter the option you want to perform: ")

    if option == "1":
        print("occurrence of a word")
        text = input("enter sentence: ")
        words = text.split()
        count = {}
        for w in words:
            count[w] = count.get(w, 0) + 1
        print(count)

    elif option == "2":
        print("character frequency")
        s = input("enter the string: ")
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        print("number of times each character appears:", count)

    elif option == "3":
        print("factors of a given number")
        n = int(input("enter a number: "))
        print("factors of", n, "are:", end=" ")
        for i in range(1, n+1):
            if n % i == 0:
                print(i, end=" ")
        print()

    elif option == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid option.")
