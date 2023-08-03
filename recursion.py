#Question (7).
''' write a recursive searching algorithm to search for a number entered by user in a list of numbers.
Recursive search algoritm  searches for a target number in a given list of numbers.
To perform this algoritm I will create a function that takes three arguments: nums (the list of numbers), target (the number to search for),
and index (the current index being checked in the list, startng with a default value of 0)'''

def recursive_search(nums, target, index=0):
    if index >= len(nums):              #checking if the current index is greater than or equal to the length of the nums list, if it is, then it means it has searched through the entire list and haven't found the target number, in this case, the function returns will return False to indicate that the target is not in the list.
        return False

    if nums[index] == target:               #checking if the current number at the index position in the nums list is equal to the target, it means  the target number is found. In this case, the function returns True to indicate that the target is in the list.
        return True

    return recursive_search(nums, target, index + 1)        #if non of the conditions above are met the function will call itself back and check the next number by incrementing the index value 1

#take user 
user_input = int(input("Enter a number to search: "))          #take user input for a number to search in the list
numbers_list = [1, 4, 8, 6, 3, 10, 7, 5, 12, 14 ,2 ,6, 9]       #list of numbers
result = recursive_search(numbers_list, user_input)             

if result:
    print(f"{user_input} is found in the list.")
else:
    print(f"{user_input} is not found in the list.")

