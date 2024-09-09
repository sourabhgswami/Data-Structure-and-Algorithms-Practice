
def find_product(nums):
# intialize left = 1 and right 1 
    left = 1
    right = 1

# intialize empty product 
    product = []

# left to right for loop , intialize loop for values in numbs 
    for values in nums:
# append value of left in product 
        product.append(left)
# update value of left by multiplying it current number
        left *= values

# right loop , right to left , Intialize a loop for product list from right to left , so range(len(prodcut)-1, -1, -1)
    for i in range(len(product)-1, -1, -1):
# multiple the value of i in product to right 
        product[i] *= right
# update value of right by multiple it to the current number
        right *= nums[i]
    
    return product 


def main():
    inputs = [
        [1, 2, 3, 4],   
        [5, -3, -1, 2],   
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