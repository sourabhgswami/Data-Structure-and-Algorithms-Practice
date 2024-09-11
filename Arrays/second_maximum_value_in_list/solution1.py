def find_second_maximum(nums):

# intialize two variables first_max and second_max as - infity 
    first_max = float("-inf")
    second_max = float("-inf")


# first tranvserse, if number greater than first_max , update first_max to current number 
    for num in nums:
        if num > first_max:
            first_max = num

#second tranvserse, if number less than first_max but greater than second_max , update second_max
    for item in nums: 
        if item != first_max and item > second_max:
            second_max = item 

#return second_max
    return second_max 

# Driver code
def main():
    inputs = [[9, 2, 3, 6],
            [1, 2],
            [-2, 2],
            [-4, -1, -9, 1, -7],
            [25, 50, 75, 100, 100]]

    for i in range(len(inputs)):
        print(i + 1, ".\tList: ", inputs[i], sep="")
        print("\n\tSecond maximum value: ", find_second_maximum(inputs[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()