def pascal_triangle(n):
    """_summary_

    Args:
        n (int): size of triangle

    Returns:
        List: Triangle shapes 
    """
    if n <= 0:
        return []

    pasTran = [[1]]  # Initialize with the first row [1]

    for i in range(1, n):
        prev_row = pasTran[-1]  # Get the previous row
        # Construct the new row by adding pairs of adjacent values from the previous row
        new_row = [1] + [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)] + [1]
        pasTran.append(new_row)

    return pasTran

