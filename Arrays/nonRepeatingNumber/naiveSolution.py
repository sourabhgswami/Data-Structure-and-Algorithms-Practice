def find_first_unique(nums):

#iterate through each element of list , pointer name p1
    for p1 in range(len(nums)):
        p2 = 0 
    #compare the current element with all other element using pointer p2 
        while (p2 < len(nums)):
        #check if there index are not same and the value is same , then break 
            if (p1 != p2 and nums[p1] == nums[p2]):
                break 
            p2 += 1

    # if p2 reach end of list, then p1 is unique
        if p2 == len(nums):
            return nums[p1]

    return None

def main():

    inputs = [
        [9, 2, 3, 2, 6, 6],
        [-5, -4, -4, 6, -1],
        [-1, 2, -1, -4, -10],
        [1, 1, 2, 9],
        [-2, 2, -2, 2, 5]
    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tInput list: ", inputs[i], sep="")
        print("\n\tfirst unique number: ", find_first_unique(inputs[i]), sep="")
        print("-" * 100)

if __name__ == "__main__":
    main()