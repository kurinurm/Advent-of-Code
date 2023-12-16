# AoC 2023 day 15, both parts
# Super simple, because Python standard dictionary retains insertion order since version 3.6

with open("data\\15.txt") as f:
    input_data = f.read().strip()

def aoc_hash(s):
    x = 0
    for c in s:
        x = ((x + ord(c)) * 17) % 256
    return(x)
   
# Part 1

sum_hashes = sum(aoc_hash(s) for s in input_data.split(","))
print("Part 1:", sum_hashes)

# Part 2

boxes = [dict() for x in range(256)]

for i, s in enumerate(input_data.split(",")):
    if "-" in s:
        lens_id = s[:s.index("-")]
        box_id = aoc_hash(lens_id)
        # print("removing", lens_id, "from box", box_id)
        if lens_id in boxes[box_id]:
            del boxes[box_id][lens_id]
    elif "=" in s:
        lens_id = s[:s.index("=")]
        box_id = aoc_hash(lens_id)
        lens_focal = int(s[s.index("=")+1:])
        boxes[box_id][lens_id] = lens_focal
        # print("adding", lens_id, "to box", box_id, "focal", lens_focal)
    else:
        print("Some error in input data", s)
        
fp = 0
for box_id, box in enumerate(boxes):
    for slot_id, lens in enumerate(box):
        fp += (box_id+1) * (slot_id+1) * box[lens]
        
print("Part 2:", fp)
