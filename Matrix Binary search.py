# ATTENTION! THE CODE BELOW DOES NOT BELONG TO ME. IT IS AN EXAMPLE OF SEARCH ALGORITHM FOR MATRICES.

def search_matrix(matrix, target):
    """
    Search for a target element in a sorted matrix.

    Parameters:
        matrix (list of lists): The sorted matrix.
        target: The element to search for.

    Returns:
        tuple: The index of the target element if found, (-1, -1) otherwise.
    """
    if not matrix:
        return -1, -1

    rows = len(matrix)
    cols = len(matrix[0])

    # Start from the top-right corner of the matrix
    row = 0
    col = cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return row, col
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1

    return -1, -1

# Example usage:
my_matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target_element = 16
row_index, col_index = search_matrix(my_matrix, target_element)

if row_index != -1 and col_index != -1:
    print(f"Element {target_element} found at position ({row_index}, {col_index}).")
else:
    print(f"Element {target_element} not found in the matrix.")
