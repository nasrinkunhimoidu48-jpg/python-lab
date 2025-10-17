def get_list(prompt):
    # Get a list of integers from user input
    return list(map(int, input(prompt).split()))

# Enter two lists from user
list1 = get_list("Enter numbers for the first list, separated by spaces: ")
list2 = get_list("Enter numbers for the second list, separated by spaces: ")

while True:
    print("\nMenu:")
    print("1. Check if lists are of the same length")
    print("2. Check if lists sum to the same value")
    print("3. Check if any value occurs in both lists")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if len(list1) == len(list2):
            print("The lists are of the same length.")
        else:
            print("The lists are not of the same length.")

    elif choice == "2":
        if sum(list1) == sum(list2):
            print("The sums of the two lists are equal.")
        else:
            print("The sums of the two lists are not equal.")

    elif choice == "3":
        common = set(list1) & set(list2)
        if common:
            print("Common values:", list(common))
        else:
            print("No common values.")

    elif choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
