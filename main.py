from game import *

def main():
    grid = init_grid()
    
    while True:
        print_grid(grid)
        
        if game_over(grid):
            print('Game over')
            break
        
        move = input('Enter next move (w: up, s: down, a: left, d: right)').strip().lower()
        
        try:
            move in ['w','s','a','d']
        except:
            print('Incorrect input')
        if move == 'w':
            grid = move_up(grid)
        elif move == 's':
            grid = move_down(grid)
        elif move == 'a':
            grid = move_left(grid)
        else:
            grid = move_right(grid)
        
        add_new_tile(grid)
        
if __name__ == '__main__':
    main()