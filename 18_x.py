# AoC 2023 day 18 Part 2

import re
with open("data\\18.txt") as f:
    input_data = f.read().split("\n")

directions = { "U":(-1,0), "D":(1,0), "R":(0,1), "L":(0,-1) }

row, col = 0, 0
line = 0 # digging path
area = 0 # area contained by path

for row_id, s in enumerate(input_data):
    if len(s) < 2:
        continue
    x = re.match("([UDRL]) (\d+) \(\#([a-f0-9]{5})([0-4])\)",s)
    p2 = "RDLU"[int(x.groups()[3])]  # direction
    d2 = int(x.groups()[2],16)       # path segment length

    new_row = row + d2*directions[p2][0]
    new_col = col + d2*directions[p2][1]    
    area += col * new_row - row * new_col
    line += d2
    row, col = new_row, new_col

print("Part 2:", area // 2 + line // 2 + 1) 
