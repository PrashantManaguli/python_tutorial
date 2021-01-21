import numpy as np
# Arrays
arr = np.array([1, 2, 3, 4, 5])
tuple = np.array((1, 2, 3, 4, 5))
# Tuples

# 2-D Arrays
twoDArray = np.array([[1, 2, 3], [4, 5, 6]])

# Copy Array
x = arr.copy()
# View Array
v = arr.view()


print("Array is : ",arr)
print("Tuple : " , tuple)
print("Array Index : ",arr[0])
print("Tuple Index : ",tuple[1:4])
print("2-D Array : ",twoDArray)
print("2-D Array Index : ",twoDArray[1,2])
print("2-D Array Index from last : ",twoDArray[1,-1])
print("Array Copy : ",x)
print("Array View : ",v[0])