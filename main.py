import numpy as np

# Set the dimensions of the grid
rows, cols = 10, 10
# Generate a 64x64 grid with random integers from 1 to 5
grid = np.random.randint(1, 6, size=(rows, cols))
# Print the grid
print(grid)

my_dict = {1: None, 2: None, 3: None, 4: None, 5: None}