import random
grid_size = 4

#initialize grid including adding new 2s
def init_grid():
    grid = [[0] * grid_size for i in range(grid_size)]
    add_new_tile(grid)
    add_new_tile(grid)
    return grid

# add new 2 to the grid
def add_new_tile(grid):
    empty_cells = [(r,c) for r in range(grid_size) for c in range(grid_size) if grid[r][c] == 0]
    if empty_cells:
        r,c = random.choice(empty_cells)
        grid[r][c] = 2
        
# print grid
def print_grid(grid):
    for row in grid:
        print(' '.join(str(num).rjust(4) if num != 0 else '    'for num in row))
    print()
    
# check if any more moves left
def game_over(grid):
    for r in range(grid_size):
        for c in range(grid_size):
            if grid[r][c] == 0:
                return False
            if c < grid_size - 1 and grid[r][c] == grid[r][c+1]:
                return False
            if r < grid_size - 1 and grid[r][c] == grid[r+1][c]:
                return False
    return True

# left aligned grid
def left_align(grid):
    new_grid = [[0]*grid_size for i in range(grid_size)]
    for r in range(grid_size):
        pos = 0
        for c in range(grid_size):
            if grid[r][c] != 0:
                new_grid[r][pos] = grid[r][c]
                pos += 1
    return new_grid

# merge cells
def merge(grid):
    for r in range(grid_size):
        for c in range(grid_size-1):
            if grid[r][c] == grid[r][c+1] and grid[r][c] != 0:
                grid[r][c] = grid[r][c] * 2
                grid[r][c+1] = 0
    return grid

# clockwise rotation
def rotate_grid(grid):
    return [[grid[grid_size - c - 1][r] for c in range(grid_size)] for r in range(grid_size)]

def move_left(grid):
    grid = left_align(grid)
    grid = merge(grid)
    grid = left_align(grid)
    return grid

def move_right(grid):
    grid = rotate_grid(rotate_grid(grid))
    grid = left_align(grid)
    grid = rotate_grid(rotate_grid(grid))
    return grid

def move_up(grid):
    grid = rotate_grid(rotate_grid(rotate_grid(grid)))
    grid = left_align(grid)
    grid = rotate_grid(grid)
    return grid

def move_down(grid):
    grid = rotate_grid(grid)
    grid = left_align(grid)
    grid = rotate_grid(rotate_grid(rotate_grid(grid)))
    return grid

    