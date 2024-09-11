def find_first_unique(nums):

#step 1: intialize empty dictionary 
    frequency = {}

#step 2: Transverse the list once to count the occurance of each number 
    for num in nums: 
#if already in dictionary, increase count 
        if num in frequency:
            frequency[num] += 1
#else if not in dictionary , add it with count of 1 
        else:
            frequency[num] = 1

#step 3: transverse the list for second time to find non repeating number 
    for num in nums:

#if the fequency of number is 1, return it as a non repeating number 
        if frequency[num] == 1:
            return num
    
    return None 

def main():

    inputs = [
        [9, 2, 3, 2, 6, 6],
        [-5, -4, -4, 6, -1],
        [-1, 2, -1, -4, -10],
        [1, 1, 2, 9],
        [-2, 2, -2, 2, 5],
        [1],
        [],
        [1,1]
    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tInput list: ", inputs[i], sep="")
        print("\n\tfirst unique number: ", find_first_unique(inputs[i]), sep="")
        print("-" * 100)

if __name__ == "__main__":
    main()