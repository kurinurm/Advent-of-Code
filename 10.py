# AoC 2023 day 10
# Both parts

with open("data\\10.txt") as f:
    input_data = f.read().split("\n")
char_s = "L" # starting tile based on my input

pipes = { "|":"NS", "-":"EW", "L":"NE", "J":"NW", "7":"SW", "F":"SE", ".":"", "S":"" }
directions = { "N":(-1,0), "S":(1,0), "W":(0,-1), "E":(0,1) }  # d_row, d_col

grid = dict()
row_max, col_max = 0, 0

# Parse input into dictionary. grid[(row,column)] = character from input
# Also find grid size (row_max, col_max) and position of S (s_row, s_col)

for row_id, s in enumerate(input_data):
    if len(s) < 2:
        continue
    row_max = max(row_max, row_id)
    for col_id, c in enumerate(s.strip()):
        if c not in pipes:
            print("error on", row_id, col_id)
            break
        col_max = max(col_max, col_id)
        if c == "S":
            grid[(row_id, col_id)] = char_s
            s_row, s_col = row_id, col_id
            continue
        grid[(row_id, col_id)] = c

row, col = s_row, s_col
last_visited = (-1, -1)
print("Start at", row, col)
tube = list()

# Crawl the tube and put it into list
for i in range(100000):
    c = grid[(row, col)]
    d1, d2 = pipes[c][0], pipes[c][1]
    row_1, col_1 = row + directions[d1][0], col + directions[d1][1] 
    row_2, col_2 = row + directions[d2][0], col + directions[d2][1]
    tube.append((row,col))
    (row, col) = (row_2, col_2) if last_visited == (row_1, col_1) else (row_1, col_1)
    last_visited = tube[-1]
    if (row,col) == (s_row, s_col):
        print("loop complete at i =", i)
        break

print("Part 1:", len(tube)//2) 

# Part 2
# scan all rows and check all tiles that don't belong to tube
# count number of passed walls, which are: | or FJ or L7 (ignoring horizontal sections)
# uneven wall count - tile must be contained by tube
# print out the grid for debug & fun

tube = set(tube) # faster membership check
inside_area = 0 

for row in range(row_max+1):
    s = ""              # printable row for debug
    c1 = ""             # starting char of walls - F or L
    wall_count = 0      # number of walls passed so far
    for col in range(col_max+1):
        if (row,col) in tube:
            c = grid[(row,col)]
            if c  == "|":
                wall_count += 1
            elif c in "FL": # start of possible wall, let's save starting char as c1
                c1 = c
            elif c == "J":
                if c1 == "F":
                    wall_count += 1
                c1 = ""
            elif c == "7":
                if c1 == "L":
                    wall_count += 1
                c1 = ""
            s += c
        else:
            if wall_count % 2 == 1:
                inside_area += 1
                s += "."
            else:
                s += " "
    print(s)

print("Part 2, area contained by tube:", inside_area)
