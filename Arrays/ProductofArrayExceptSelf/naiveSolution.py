def find_product(nums):
    #empty list to store the product of all the numbers 
    product = []

    #initalize left to 1 
    left = 1

    # for loop to iterate through the list 
    for i in range(len(nums)):
        current_product = 1


    # find the product of all the numbers on the right side 
        for values in nums[i+1:]:
            current_product *= values

    # Multiplt the products of the right side to the left 
        current_product *= left
    
    # Append it to the product list 
        product.append(current_product)

    # update left to left * nums[i]
        left *= nums[i]

    #return the product list
    return product 

def main():
    inputs = [
        [1, 2, 3, 4],   
        [5, -3, 1, 2],   
        [2, 2, 2, 0],      
        [0, 0, 0, 0],   
        [-1, -2, -4]   
    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tArray: ", inputs[i], sep="")
        print("\n\tList of products: ", find_product(inputs[i]), sep="")
        print("-" * 100)

if __name__ == "__main__":
    main()