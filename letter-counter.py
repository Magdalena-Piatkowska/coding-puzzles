#Counts the count of a letter in a string. Inspired by SoloLearn's "Beginner Python" course.

print("Let's take a word and a letter and check how many times said letter appears in said word. \n")
word = str(input("Please provide a word: \n"))
letter = input("Please provide a letter: \n")

def letter_counter(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count

print(letter_counter(word, letter))