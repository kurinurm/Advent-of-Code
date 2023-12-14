# AoC 2023 day 13

with open("data\\13.txt") as f:
    input_data = f.read().split("\n")

new_grid = True
grid_id = 0
grid = []
all_grids = []
sum_splits = 0

# Import all grids into a list all_grids 
for row_id, s in enumerate(input_data):
    if len(s) < 2:
        if grid:
            all_grids.append(grid)
        new_grid = True
        grid_id += 1
        grid = []
        continue
    new_grid = False
    tmp_row = []
    for c in s.strip():
        if c in "#.":
            tmp_row.append(c)
    grid.append(tmp_row)


# Find all splitting lines in grid g
# Return a list of lists, eg [["v",3], ["h",5]]

def find_split(g):

    all_found_splits = []
    global sum_splits
    
    max_row = len(g)
    max_col = max(len(row) for row in g)
    
    rows = []
    for row_pos in range(max_row):
        row_bitvalue = 0
        for col_pos in range(max_col):
            c = g[row_pos][col_pos]
            row_bitvalue <<= 1
            row_bitvalue += 1 if c == "#" else 0
        rows.append(row_bitvalue)
    if len(rows) > len(set(rows)):
        rr = ""
        for i, x in enumerate(rows[:-1]):
            rr += str(x)
            rr += " "
            if x == rows[i+1]:
                # potential horizontal split between pos i and i+1, let's check
                is_split = True
                for j in range(len(rows)):
                    if i-j < 0:
                        break
                    if i+1+j >= len(rows):
                        break
                    if rows[i-j] != rows[i+1+j]:
                        is_split = False
                if is_split:
                    all_found_splits.append(["h",i])
            
    cols = []
    for col_pos in range(max_col):
        col_bitvalue = 0
        for row_pos in range(max_row):
            c = g[row_pos][col_pos]
            col_bitvalue <<= 1
            col_bitvalue += 1 if c == "#" else 0
        cols.append(col_bitvalue)
    if len(cols) > len(set(cols)):
        rr = ""
        for i, x in enumerate(cols[:-1]):
            rr += str(x)
            rr += " "
            if x == cols[i+1]:
                is_split = True
                for j in range(len(cols)):
                    if i-j < 0:
                        break
                    if i+1+j >= len(cols):
                        break
                    if cols[i-j] != cols[i+1+j]:
                        is_split = False
                if is_split:
                    all_found_splits.append(["v",i])
       
    return all_found_splits

sum_splits = 0
sum_fixed_splits = 0

# For all grids:
# - find a split in original grid
# - treat any location as possible smudge, flip it and re-check for splits

for grid_id, g in enumerate(all_grids):
    splits = find_split(g)
    if len(splits) == 0:
        print("No splits, hmm.")
    elif len(splits) > 1:
        print("Multiple splits, hmm.")
    elif len(splits) == 1:
        sum_splits += (splits[0][1]+1) * ( 1 if splits[0][0] == "v" else 100 )
        
    max_row = len(g)
    max_col = max(len(row) for row in g)

    for row in range(max_row):
        for col in range(max_col):
            g[row][col] = "." if g[row][col] == "#" else "#" # "fix" or flip smudge 
            s = find_split(g)
            g[row][col] = "." if g[row][col] == "#" else "#" # flip smudge back
            if not s or s == splits:
                continue
            s = [x for x in s if x not in splits] # exclude the original un-smudged reflection line
            if len(s) > 1:
                print("Multiple splits, hmm.")
                continue
            sum_fixed_splits += (s[0][1]+1) * ( 1 if s[0][0] == "v" else 100 )
            
    splits = find_split(g)

print("Part 1:", sum_splits)
print("Part 2:", sum_fixed_splits // 2)  # /2 because every smudge has a "mirror" smudge
