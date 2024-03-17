#2d array
a.dtype # dtype of the elements in the array
a = np.array([[1,2],[3,4],[5,6]], dtype = np.float64) # specify data type while creating an array
print(a.itemsize)#itemsize means the number of items in the array along each dimension (in bytes)
print(a.ndim)# ndim means number of dimensions in the array   
print(a)