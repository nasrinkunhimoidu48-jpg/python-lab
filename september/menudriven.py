count = 0;

while ( count != 1):
    var = int(input("Choose Options \n1. Occurence of word \n2. Character frequency \n3. Display the factors of a given number \n4. Exit\n\n"))

    if var == 1:
        a = input("Enter a Text: ")
        b = a.split()
        s = set(b)
        for i in s:
            print(i, "=", b.count(i))
    elif var == 2:
        a = input("Enter a Text: ")
        s = set(a)
        for i in s:
            print(i, "=", a.count(i))
    elif var == 3:
        a = int(input("Enter a Number: "))
        print(f"factors of {a} are: ")
        for i in range(1, a+1):
            if a % i == 0:
                print(i)
    elif var == 4:
         print("Exited...")
         count = 1
    else:
        print("Invalid Number!!!")
