def right_rotate(nums, k): 

    #check list length, if 0 - return same list else, count the effective roation amount by module to list length 
    if k == 0:
        return nums 
    else:
        k = k % len(nums)

    #intialize new list to store element 
    rotatedlist = []

    #check elements at the end and put them in new list 
    for items in range(len(nums) - k , len(nums)):
        rotatedlist.append(nums[items])


    #get the remaning elements and put them in rotated list 
    for items in range(0, len(nums)-k):
        rotatedlist.append(nums[items])

    return rotatedlist

def main():
    inputs = [
        ([10, 20, 30, 40, 50]),  
        ([1, -2, 3, 4, 5]),  
        ([-1, 90, -90, 4, 6]),      
        ([3, 6, 9, -12]),          
        ([-100, -200, -300])         
    ]
    k= [3, 2, 6, 2, 1]
    
    for i in range(len(inputs)):
        print(i + 1, ".\tnums: ", inputs[i], sep="")
        print("\tk: ", k[i], sep="")
        print("\n\tRotated list: ", right_rotate(inputs[i], k[i]), sep="")
        print("-" * 70)

if __name__ == "__main__":
    main()
