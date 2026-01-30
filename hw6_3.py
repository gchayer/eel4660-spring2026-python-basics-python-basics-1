# Write a function called average that takes a list of numbers as a parameter
# and returns the average of the numbers in the list.

def average(numlist):
    return sum(numlist)/len(numlist)

if __name__ == "__main__":
    print(average([1, 2, 3, 4, 5]))  # 3.0