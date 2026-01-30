# Write a function sumEven(lst) to sum up all the even numbers in a list.

def sumEven(lst):
    return sum(num for num in lst if num%2==0)

if __name__ == "__main__":
    print(sumEven([1, 2, 3, 4, 5]))  # 6
    print(sumEven([2, 4, 6, 8, 10]))  # 30
    print(sumEven([1, 3, 5, 7, 9]))  # 0