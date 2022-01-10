# Returns a string sans vowels. Inspired by SoloLearn's "Intermediate Python" course.

print("Let's take a word and see what it looks like without any vowels in it. \n")

# 1st solution. Uses a for loop.
print([char for char in input("Please provide a word: \n") if char.lower() not in "aeiou"])


# 2nd solution. Uses a lambda function and a built-in filter() function.
# print(list(filter(lambda char: char.lower() not in "aeiou", input("Please provide a word: \n"))))
