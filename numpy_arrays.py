import numpy

def arrays(arr):
    array = numpy.array(arr)
    flipped_array = numpy.flip(array)
    return flipped_array.astype(float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)