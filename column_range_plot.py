import numpy as np
import matplotlib.pyplot as plt

def column_range_plot(A, filename="column_ranges.pdf"):
    A = np.array(A)
    col_ranges = []

    for j in range(A.shape[1]):
        column_values = A[:, j]
        r = max(column_values) - min(column_values)
        col_ranges.append(r)
        
    col_ranges = np.array(col_ranges)
    
    plt.figure()
    plt.bar(range(A.shape[1]), col_ranges, color='gray')
    plt.title("Column Ranges")
    plt.xlabel("Column Index")
    plt.ylabel("Range")
    plt.savefig(filename)
    plt.show 
    plt.close
    return col_ranges

A = np.array([
    [1, 5, 3],
    [4, 2, 8],
    [7, 9, 1]
])

ranges = column_range_plot(A, filename="example_column_ranges.pdf")
print("Column ranges:", ranges)
