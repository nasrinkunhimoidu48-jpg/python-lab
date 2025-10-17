# Read a sentence from the user
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# (a) Count the number of words
print("Number of words:", len(words))

# (b) Search for a particular word
search_word = input("Enter the word to search for: ")
count = words.count(search_word)
print(f"The word '{search_word}' appears {count} times.")
