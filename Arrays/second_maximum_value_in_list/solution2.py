def find_second_maximum(nums):
    #initalize two variable to negative infinity 
    first_max = float("-inf")
    second_max = float("-inf")

    #iterate through each element of list 
    for num in nums:
    #if current element is greater than first_max , then update second max value to first max and first max value to current element 
        if num > first_max:
            second_max = first_max 
            first_max = num 
    # if current element is greater than second man , then update value to second max 
        elif num > second_max:
            second_max = num 

    #return second max value 
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