
import numpy as np

q=np.array(([1,2,3,4,5],[6,7,8,9,10]))

print(q)

f=np.ndarray.flatten(q)

print("the flattened array is ",f)

max=f.max()

min=f.min()

print("the max and min value of flattened
