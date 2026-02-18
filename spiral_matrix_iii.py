def spiralMatrixIII(rows, cols, rStart, cStart):
    # 1. Directions: EAST, SOUTH, WEST, NORTH
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # 2. Result list to store positions inside the grid
    result = []
    
    # 3. Start from the initial position
    r, c = rStart, cStart
    
    # 4. Add the starting position
    result.append([r, c])
    
    # 5. Steps we take in each direction
    step_size = 1  # initial step size
    
    # 6. Continue until we collect all positions
    while len(result) < rows * cols:
        # Loop over the 4 directions
        for i in range(4):
            # Meaningful step: first 2 directions use current step_size,
            # next 2 directions use step_size + 1
            steps = step_size if i < 2 else step_size + 1
            
            # Move in the current direction
            for _ in range(steps):
                r += directions[i][0]  # row change
                c += directions[i][1]  # column change
                
                # Only add if inside the grid
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
        
        # After completing all 4 directions, increase step_size by 2
        # so spiral expands correctly in the next loop
        step_size += 2
    
    return result

# Example usage:
print(spiralMatrixIII(3, 3, 1, 1))
