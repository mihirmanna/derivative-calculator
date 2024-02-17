def matrix_vector_product(matrix: list[list], vector: list):
    dimension = len(matrix)
    result = [0] * dimension
    
    for i in range(dimension):
        for j in range(dimension - 1):
            result[i] += matrix[i][j] * vector[j]
    
    return result


def power_rule(equation: list):
    # Create a blank matrix for the derivative transformation
    dimension = len(equation)
    matrix = []
    for i in range(dimension):
        matrix.append([0] * dimension)
        
    # Populate the matrix
    for row in range(dimension):
        for col in range(dimension):
            if col == row + 1:
                matrix[row][col] = col
    
    return matrix_vector_product(matrix, equation)


def reverse_power_rule(equation: list):
    # Create a blank matrix for the integral transformation
    dimension = len(equation)
    matrix = []
    for i in range(dimension + 1):
        matrix.append([0] * dimension)

    # Populate the matrix
    for row in range(dimension + 1):
        for col in range(dimension):
            if not row == 0 and col == row - 1:
                matrix[row][col] = 1 / row

    return matrix_vector_product(matrix, equation)
    

if __name__ == "__main__":
    eqn = [1, 2, 3, 4]  # Corresponds to 1 + 2x + 3x^2 + 4x^3
    
    print("Equation: " + str(eqn))
    print("Derivative: " + str(power_rule(eqn)))  # [2, 6, 12, 0] corresponds to 2 + 6x + 12x^2
    print("Integral: " + str(reverse_power_rule(eqn)))  # [0, 1, 1, 1, 1] corresponds to x + x^2 + x^3 + x^4
    