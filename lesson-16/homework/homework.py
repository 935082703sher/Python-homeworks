import numpy as np

# Define the structured data type
dtype = np.dtype([
    ('position', [('x', 'f4'), ('y', 'f4')]),
    ('color', [('r', 'u1'), ('g', 'u1'), ('b', 'u1')])
])

# Create the structured array
data = np.array([
    ((10.0, 20.0), (255, 0, 0)),
    ((30.5, 40.5), (0, 255, 0)),
    ((50.2, 60.3), (0, 0, 255))
], dtype=dtype)

# Example: Accessing the array
print(data)
print("First position:", data[0]['position'])
print("First color:", data[0]['color'])
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
import numpy as np
from scipy.spatial import distance_matrix  # convenient for point-to-point distances

# Generate random coordinates (100 points in 2D)
points = np.random.rand(100, 2)

# Compute pairwise distances using scipy
distances = distance_matrix(points, points)

print(distances.shape)  # Should be (100, 100)
print(distances)        # Pairwise distances between points.
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
import numpy as np

# Example float32 array
arr = np.array([1.7, 2.3, 3.9], dtype=np.float32)

# Overwrite the array with converted integers
arr[:] = arr.astype(np.int32)

print(arr)
print(arr.dtype)  # Still float32! Just values replaced with integers.
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
import numpy as np

# Example float32 array
arr = np.array([1.7, 2.3, 3.9], dtype=np.float32)

# Overwrite the array with converted integers
arr[:] = arr.astype(np.int32)

print(arr)
print(arr.dtype)  # Still float32! Just values replaced with integers.
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
import numpy as np
data = np.genfromtxt('data.csv', delimiter=',', dtype=np.float32)
print(data)
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
import numpy as np
arr = np.array([[10, 20], [30, 40]])
for index, value in np.ndenumerate(arr):
    print(index, value)
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
import numpy as np

def gaussian_2d(shape=(100, 100), center=None, sigma=10):
    """Generates a 2D Gaussian-like array."""
    x = np.arange(0, shape[1], 1, float)
    y = np.arange(0, shape[0], 1, float)
    y = y[:, np.newaxis]

    if center is None:
        center = (shape[1] / 2, shape[0] / 2)
    return np.exp(-((x - center[0])**2 + (y - center[1])**2) / (2 * sigma**2))
gauss = gaussian_2d(shape=(100, 100), sigma=25)
print(gauss)

import matplotlib.pyplot as plt



plt.title('2D Gaussian')
plt.show()
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
import numpy as np

# Define your array shape and number of elements to place
shape = (5, 5)
p = 7  # number of elements to randomly place

# Create the flat indices for the total array size
total_elements = shape[0] * shape[1]
indices = np.random.choice(total_elements, p, replace=False)
print(indices)
# Create the array and place the elements
array = np.zeros(shape, dtype=int)
print(array)
array.flat[indices] = 1  # flat allows you to index the array as if it were 1D

print(array)
'''[16 22 20 24 11  2 19]
[[0 0 1 0 0]
 [0 0 0 0 0]
 [0 1 0 0 0]
 [0 1 0 0 1]
 [1 0 1 0 1]]
 [21 17 24  0  2 11  1]
[[1 1 1 0 0]
 [0 0 0 0 0]
 [0 1 0 0 0]
 [0 0 1 0 0]
 [0 1 0 0 1]]
 axis=0 (↓) | Down the columns (vertical)
axis=1 (→) | Across the rows (horizontal).
 '''
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
import numpy as np
# Example matrix
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
# Compute the mean of each row (keepdims=True keeps shape for broadcasting)
row_means = X.mean(axis=1, keepdims=True)
# Subtract the mean of each row from its elements
X_centered = X - row_means
print(X_centered,row_means)
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
import numpy as np

# Example 2D array
arr = np.array([[3, 7, 1],
                [2, 5, 9],
                [8, 6, 4]])


n = 0  # Column index to sort by (0-based)

# Use argsort on the nth column
sorted_arr = arr[arr[:, n].argsort()]

print(sorted_arr)
# Reverse the columns because lexsort sorts by last key first!
indices = np.lexsort((arr[:, 2], arr[:, 1], arr[:, 0]))
sorted_arr = arr[indices]

print(sorted_arr)
indices = np.lexsort([arr[:, i] for i in reversed(range(arr.shape[1]))])
sorted_arr = arr[indices]
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
import numpy as np

# Example array
arr = np.array([[0, 1, 0],
                [0, 2, 0],
                [0, 3, 0]])

# Check if any column is entirely zero:
null_columns = np.all(arr == 0, axis=0)

print(null_columns)  # True where the column is all zeros
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
import numpy as np

# Example array
arr = np.array([10, 20, 30, 40, 50])

# The target value
target = 43

# Find the index of the closest value
index = np.abs(arr - target).argmin()
print(index)
# Get the nearest value
nearest_value = arr[index]

print(f"Nearest value {target} is {nearest_value}")
#5555555555555555555555555555555555555555555yyyyyyyyyyyyyyyyymmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
import numpy as np

a = np.array([[1, 2, 3]])
b = np.array([[4], [5], [6]])

result = np.empty((3, 3), dtype=int)  # create empty array for results
print(result)
# Setup iterator with multi-indexing and broadcasting
it = np.nditer([a, b, result], flags=['multi_index', 'refs_ok', 'reduce_ok'],
               op_flags=[['readonly'], ['readonly'], ['writeonly']])

for x, y, z in it:
    z[...] = x + y  # element-wise addition

print(result)
result = a + b  # Broadcasting does this automatically!
result = a + b  # Broadcasting does this automatically!
result
#==============================================================================99{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}
import numpy as np

class NamedArray(np.ndarray):
    def __new__(cls, input_array, name="unnamed"):
        # Convert input_array to ndarray instance
        obj = np.asarray(input_array).view(cls)
        # Add the new attribute
        obj.name = name
        return obj

    def __array_finalize__(self, obj):
        # When creating new views, copy the name attribute if present
        if obj is None: return
        self.name = getattr(obj, 'name', "unnamed")

# Example usage:
arr = NamedArray([[1, 2, 3], [4, 5, 6]], name="my_matrix")

print(arr)
print("Name of array:", arr.name)
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
import numpy as np

# Main vector
x = np.array([0, 0, 0, 0, 0])

# Indices where we want to add 1 (with repeats!)
indices = np.array([1, 3, 1, 2, 1])

# Correct way to add 1 at these indices (handling repeats properly)
np.add.at(x, indices, 1)

print(x)
#33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
import numpy as np

# The values you want to accumulate:
X = np.array([5, 3, 2, 7, 1])

# The indices where each value should be added:
I = np.array([0, 1, 1, 2, 0])  # repeated index '0' and '1' here!

# Target array where accumulation happens:
F = np.zeros(3, dtype=int)  # Assume we have 3
print(F)
np.add.at(F, I, X)

print(F)
##333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
import numpy as np

# Example: random image of shape (w, h, 3)
w, h = 100, 100
image = np.random.randint(0, 256, size=(w, h, 3), dtype=np.uint8)

# Reshape the image to a 2D array where each row is a color (R, G, B)
pixels = image.reshape(-1, 3)

# Find unique colors
unique_colors = np.unique(pixels, axis=0)

# Count them
num_unique_colors = unique_colors.shape[0]
import matplotlib.pyplot as plt
print(f"Number of unique colors: {num_unique_colors}")
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
import numpy as np

# Example 4D array
arr = np.random.rand(3, 4, 5, 6)  # shape (3, 4, 5, 6)
print(arr)
# Sum over the last two axes (axes 2 and 3)
result = np.sum(arr, axis=(2, 3))
print(result)
print(result.shape)  # → (3, 4)
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
import numpy as np

# Your data vector:
D = np.array([5, 6, 7, 8, 9])

# Subset labels:
S = np.array([0, 1, 0, 1, 0])  # Same length as D
sum_per_group = np.bincount(S, weights=D)
count_per_group = np.bincount(S)
mean_per_group = sum_per_group / count_per_group

print(mean_per_group)
#=================================================================================================================
import numpy as np

# Example matrices
A = np.random.rand(4, 3)  # shape (4, 3)
B = np.random.rand(3, 4)  # shape (3, 4)

# Compute only the diagonal of A @ B
diagonal = np.einsum('ij,ji->i', A, B)

print(diagonal)
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
import numpy as np

# Original vector
v = np.array([1, 2, 3, 4, 5])
# Number of zeros between values
n_zeros = 3
# Total length: each value + 3 zeros between → need (len(v) - 1) * (n_zeros + 1) + 1 slots
new_length = len(v) + n_zeros * (len(v) - 1)
result = np.zeros(new_length, dtype=int)
# Place original values at the correct positions
result[::n_zeros + 1] = v
print(result)
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
m=np.random.rand(5,5)
m1=np.random.rand(5,5,3)
e=m[:,:,np.newaxis]*m1
print(e)
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
import numpy as np
# Create example array
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
# Swap row 0 and row 2
A[[0, 2]] = A[[2, 0]]

print(A)
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
import numpy as np

# 10 triangles, each triangle defined by 3 vertex indices
triangles = np.random.randint(0, 20, (10, 3))
print(triangles)
edges = []

# Extract edges from triangles
for tri in triangles:
    a, b, c = tri
    edges.append(tuple(sorted((a, b))))
    edges.append(tuple(sorted((b, c))))
    edges.append(tuple(sorted((c, a))))

# Remove duplicates by converting to set
unique_edges = set(edges)
print(unique_edges)
import numpy as np

# 10 triangles, each triangle defined by 3 vertex indices
triangles = np.random.randint(0, 20, (10, 3))
print(triangles)
edges = []

# Extract edges from triangles
for tri in triangles:
    a, b, c = tri
    print(edges.append(tuple(sorted((a, b)))))
    edges.append(tuple(sorted((b, c))))
    edges.append(tuple(sorted((c, a))))

# Remove duplicates by converting to set
unique_edges = set(edges)
print(unique_edges)
#[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
import numpy as np

C = np.array([2, 0, 3])

# Create array A where each index is repeated C[index] times
A = np.repeat(np.arange(len(C)), C)

print(A)








