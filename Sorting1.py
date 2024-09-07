#!/usr/bin/env python
# coding: utf-8

# 1.Given an array of n numbers, give an algorithm which gives the element appearing maximum
# number of times?

# In[1]:


def mostFrequent(arr, n): 
  
    # Sort the array 
    arr.sort() 
  
    # find the max frequency using linear traversal 
    max_count = 1
    res = arr[0] 
    curr_count = 1
  
    for i in range(1, n): 
        if (arr[i] == arr[i - 1]): 
            curr_count += 1
        else: 
            curr_count = 1
  
         # If last element is most frequent 
        if (curr_count > max_count): 
            max_count = curr_count 
            res = arr[i - 1] 
  
    return res 
  
  
# Driver Code 
arr = [40,50,30,40,50,30,30] 
n = len(arr) 
print(mostFrequent(arr, n)) 
  


# 2 : We are given a list of n-1 integers and these integers are in the range of 1 to n . There are no
# duplicates in the list. One of the integers is missing in the list. Give an algorithm to find that element Ex:
# [1,2,4,6,3,7,8] 5 is the missing num.

# In[2]:


def missing_number(n, arr):
    sum_arr = sum(arr)
    # Calculate the expected sum
    expected_sum = (n * (n + 1)) // 2
    # Return the missing number
    return expected_sum - sum_arr


# Driver code
arr =  [1,2,4,6,3,7,8] 
n = 8
print(missing_number(n, arr))


# 3 : Given an array of n positive numbers. All numbers occurs even number of times except 1 which
# occurs odd number of times. Find that number in O(n) time and O(1) space. Ex: [1,2,3,2,3,1,3]. 3 is repeats odd
# times.

# In[3]:



# Python program to find the element occurring odd number of times

def getOddOccurrence(arr):

# Initialize result
    res = 0

    # Traverse the array
    for element in arr:
        # XOR with the result
        res = res ^ element

    return res

    # Test array
    arr = [ 1,2,3,2,3,1,3]

    print("%d" % getOddOccurrence(arr))


# 4 : Given an array of n elements. Find two elements in the array such that their sum is equal to given element K.
# 
# 

# In[13]:


def sum(arr):
    search=[]
    k=7
    for i in arr:
        x=arr[i]-k
        if x in search:
            return x,i
    return search.append(arr[i])
         
arr=[2,3,6,7]
print(sum(arr))


# 5 : Given an array of both positive and negative numbers, find two numbers such that their sum is
# closest to 0. Ex: [ 1 ,60 ,-10, 70, -80,85]. Ans : -80,85.

# In[10]:


def zero(arr):
    for i in arr:
        if arr[i]+arr[i+1]==0:
            return i,i+1
        
        


#  6 : Given an array of n elements . Find three elements such that their sum is equal to the given
# number.

# In[14]:


# Function to find a triplet with a given sum in an array
def find3Numbers(arr, sum):
    n = len(arr)

    # Fix the first element as arr[i]
    for i in range(n - 2):

        # Fix the second element as arr[j]
        for j in range(i + 1, n - 1):

            # Now look for the third number
            for k in range(j + 1, n):

                if arr[i] + arr[j] + arr[k] == sum:

                    # Triplet is found; print the triplet elements
                    print(f"Triplet is {arr[i]}, {arr[j]}, {arr[k]}")
                    return True

    # If no triplet is found, return false
    return False


# Driver code
arr = [1, 4, 45, 6, 10, 8]
sum = 22

find3Numbers(arr, sum)


# 7 : Given an array of n elements . Find three elements i, j, k in the array such that
# i * i + j * j = k*k.

# In[ ]:
def find_pythagorean_triplet(arr):
    # Square each element and store it in a set for quick lookup
    squared_values = set(x * x for x in arr)
    
    # Check all pairs (i, j) and see if k^2 = i^2 + j^2 exists
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            sum_of_squares = arr[i] ** 2 + arr[j] ** 2
            if sum_of_squares in squared_values:
                k = int(sum_of_squares ** 0.5)  # Get the square root of sum_of_squares
                if k in arr:  # Check if the square root exists in the array
                    return arr[i], arr[j], k  # Return the triplet
    
    return None  # Return None if no triplet is found

# Example usage
arr = [3, 1, 4, 6, 5]
triplet = find_pythagorean_triplet(arr)
triplet if triplet else "No triplet found"






# 8 : An element is a majority if it appears more than n/2 times. Give an algorithm takes an array of n
# element as argument and identifies a majority (if it exists).

# In[ ]:
def find_majority_element(arr):

    candidate = None
    count = 0
    
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    if arr.count(candidate) > len(arr) // 2:
        return candidate
    else:
        return None

arr = [2, 2, 1, 1, 2, 2, 2]
majority_element = find_majority_element(arr)
majority_element if majority_element else "No majority element"





# 9 : Given n × n matrix, and in each row all 1’s are followed by 0’s. Find the row with the maximum
# number of 0’s.

# In[ ]:
def find_row_with_max_zeros(matrix):
    n = len(matrix)
    
    
    row = 0
    col = n - 1
    max_zero_row = -1  

    
    while row < n and col >= 0:
        if matrix[row][col] == 0:
            max_zero_row = row
            col -= 1
        else:
            row += 1

    return max_zero_row


matrix = [
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0],
    [0, 0, 0, 0]
]

max_zero_row = find_row_with_max_zeros(matrix)
max_zero_row if max_zero_row != -1 else "No zeros found"





# Problem 10 : Sort an array of 0’s, 1’s and 2’s [or R’s, G’s and B’s]: Given an array A[] consisting of 0’s, 1’s and
# 2’s, give an algorithm for sorting A[].The algorithm should put all 0’s first, then all 1’s and finally all 2’s at the
# end. Example Input = {0,1,1,0,1,2,1,2,0,0,0,1}, Output = {0,0,0,0,0,1,1,1,1,1,2,2}.

# In[ ]:

def dutch_national_flag(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1

            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1

    return arr

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sorted_arr = dutch_national_flag(arr)
sorted_arr






