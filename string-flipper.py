# All the ways of flipping a string that I could find. Inspired by SoloLearn's "Python for Beginners" course.

print("Let's take a word and flip it. \n")
word = input("Please provide a word that you want flipped: \n")

#1st solution. The simplest one. Uses list slices.
print(word[::-1])


# 2nd solution. Creates a flip_a_string() function that iterates through the string with a for loop.
# def flipping_a_string(a_string_to_be_flipped):
#     flipped_string = ""
#     for letter in a_string_to_be_flipped:
#         flipped_string = letter + flipped_string
#     return flipped_string
#
# print(flipping_a_string(word))


# 3rd solution. Iterates through the string with a for loop. Uses the in-build range() function to 'move' backwards along the string's elements.
# for letter in range(len(word)-1, -1, -1):
#     print(word[letter], end="")


# 4th solution. Much like the 3rd solution. Uses in-build join() function to join all of the iterated elements into a string.
# print("".join(word[letter] for letter in range(len(word)-1, -1, -1)))


# 5th solution
# Credits to this one go to one of the commenters on SoloLearn forum (apologies, I can't find the OP at this time).
# It's a bit less intuitive to me.
# It uses the in-build reversed() function. After turning the string into a list, you need to use the star operator (*) to unpack its elements.
# print(*reversed(list(word)), sep="")
