def cell_colony(cells, days):
    for _ in range(days):
        new_cells = [0] * 8
        
        for i in range(8):
            left = cells[i-1] if i > 0 else 0
            right = cells[i+1] if i < 7 else 0
            
            if left == right:
                new_cells[i] = 0
            else:
                new_cells[i] = 1
        
        cells = new_cells
    
    return cells


# Example
cells = [1, 0, 0, 0, 0, 1, 0, 0]
days = 1

print(cell_colony(cells, days))
