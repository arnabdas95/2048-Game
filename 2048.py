import random

# define 2048 grid 4*4
rows, cols = (4, 4)
grid = [[0 for i in range(rows)] for j in range(cols)]
# end_game flag for infinite loop
not_end = True

# check for end of game
# if all the cells are full and no 2048
def check_full_grid():
    zero_flag = True
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                zero_flag = True
            elif grid[i][j] == 2048:
                print("CONGO ..... You Win")
                end_game()
    if not zero_flag:
        print("You loose .... Better Luck Next Time")
        end_game()


def end_game():
    # not_end is for the flag for infinite loop stop
    not_end = False
    exit()


# display grid
def display_grid():
    print("------------------------------")
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                print("  |    ", end="")
            else:
                print(" | ", grid[i][j], " ", end="")
        print("|\n------------------------------")


# define random function that produce 2 or 4 in blank cell
get_num_list = [2, 4]
def get_num():
    return random.choice(get_num_list)


# define random empty cell where random number will generate
def get_random_grid():
    return random.randrange(0, 16)


# devide the get_random_grid into row and coloum
# find blank cell
def new_num_assign():

    row = get_random_grid()
    new_col = row % 4
    new_row = row // 4
    if grid[new_row][new_col] == 0:
        grid[new_row][new_col] = get_num()
    else:
        new_num_assign()


# left swipe
def left_swap():
    for i in range(rows):
        temp = []
        for j in range(cols):
            if grid[i][j] != 0:
                temp.append(grid[i][j])
                grid[i][j] = 0
        for assign_num in range(len(temp)):
            grid[i][assign_num] = temp[assign_num]




# right swipe
def right_swap():

    for i in range(rows):
        temp = []
        for j in range(cols):
            if grid[i][j] != 0:
                temp.append(grid[i][j])
                grid[i][j] = 0
        for assign_num in range(len(temp)):
            grid[i][cols - len(temp) + assign_num] = temp[assign_num]




# down swipe
def down_swap():
    for j in range(rows):
        temp = []
        for i in range(cols):
            if grid[i][j] != 0:
                temp.append(grid[i][j])
                grid[i][j] = 0
        for assign_num in range(len(temp)):
            grid[rows - len(temp) + assign_num][j] = temp[assign_num]


def up_swap():
    for j in range(rows):
        temp = []
        for i in range(cols):
            if grid[i][j] != 0:
                temp.append(grid[i][j])
                grid[i][j] = 0
        for assign_num in range(len(temp)):
            grid[assign_num][j] = temp[assign_num]


# left blending function
def left_blend():
    for i in range(rows):
        for j in range(cols-1):
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                grid[i][j] = 2 * grid[i][j]
                grid[i][j + 1] = 0
    left_swap()


# right blending function
def right_blend():
    for i in range(rows):
        for j in range(cols - 1, 0, -1):
            if grid[i][j] == grid[i][j - 1] and grid[i][j] != 0:
                grid[i][j] = 2 * grid[i][j]
                grid[i][j - 1] = 0
    right_swap()


# up_blend
def up_blend():
    for i in range(cols):
        for j in range(rows-1):
            if grid[j][i] == grid[j + 1][i] and grid[j][i] != 0:
                grid[j][i] = 2 * grid[j][i]
                grid[j + 1][i] = 0
    up_swap()


def down_blend():
    for i in range(cols):
        for j in range(rows - 1, 0, -1):
            if grid[j][i] == grid[j - 1][i] and grid[j][i] != 0:
                grid[j][i] = 2 * grid[j][i]
                grid[j - 1][i] = 0
    down_swap()


def start_game():
    new_num_assign()
    new_num_assign()
    while not_end:
        display_grid()
        x = int(input())
        if x == 2:
            down_swap()
            down_blend()
            new_num_assign()
            check_full_grid()
        elif x == 8:
            up_swap()
            up_blend()
            new_num_assign()
            check_full_grid()
        elif x == 4:
            left_swap()
            left_blend()
            new_num_assign()
            check_full_grid()
        elif x == 6:
            right_swap()
            right_blend()
            new_num_assign()
            check_full_grid()
        else:
            print("wrong entry.Try again")


if (__name__ =="__main__"):
    start_game()
