import numpy as np

def line_to_array():
    with open("text.txt", "r") as f:
        lines = f.read().splitlines()
        collection = np.array(lines)
    print(collection)

line_to_array()