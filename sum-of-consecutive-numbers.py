#Counts the sum of consecutive numbers. Inspired by SoloLearn's "Beginner Python" course.

print("Let's take a number N and output the sum of all numbers from 1 to N (including N). \n")
N = int(input("Please provide a number: \n"))


#1st solution
print(sum(range(1, N+1)))


#2nd solution
#count = 0
#result = 0
#operative = 0
#
#for operative in range(1, N+1):
#    count += 1
#    result += count
#
#print(result)
