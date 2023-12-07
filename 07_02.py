# AoC 2023 day 7
#
# Part 1: create a function to compare hands and use this as custom key for sort()
# Part 2: replace all cards in hand with J and find the strongest resulting combination

from functools import cmp_to_key   # to get sort key from comparison function
from collections import Counter    # easy count of cards in hand

with open("data\\07.txt") as f:
    input_data = f.read().split("\n")

card_strengths = {
    "A":"A",
    "K":"B",
    "Q":"C",
    "J":"x", # part 2 
    "T":"E",
    "9":"a",
    "8":"b",
    "7":"c",
    "6":"d",
    "5":"e",
    "4":"f",
    "3":"g",
    "2":"h",
}

hand_ranks = { # for debug & printouts only
    1 : "5 of a kind",
    2 : "4 of a kind",
    3 : "full house",
    4 : "3 of a kind",
    5 : "two pairs",
    6 : "one pair",
    7 : "no combination"
}

# Calculate rank of hand, 1 .. 7
def hand_rank(hand): 
    final_rank = 99

    # replace any char with J and calculate max rank

    for c in hand:
        hand_tmp = hand.replace("J", c) # also replaces J-s with J

        h = set(hand_tmp)
        c = Counter(hand_tmp)
        
        if len(h) == 1:
            rank = 1
        elif len(h) == 2:
            if max(c.values()) == 4:
                rank = 2
            else:
                rank = 3
        elif len(h) == 3:
            if max(c.values()) == 3:
                rank = 4
            else:
                rank = 5
        elif len(h) == 4:
            rank = 6
        elif len(h) == 5:
            rank = 7 

        final_rank = min(rank, final_rank)

    # Hand with hand type prefixed and cards replaced by strengh, eg KKKJA => 2-BBBxA (4 of a kind)
    hh = str(final_rank) + '-' + ''.join([card_strengths[x] for x in hand])
    
    return(final_rank, hh)
    
# Comparator for two hands

def compare(hand1, hand2):
    r1, h1 = hand_rank(hand1)[0], hand_rank(hand1)[1]
    r2, h2 = hand_rank(hand2)[0], hand_rank(hand2)[1]
    return -1 if h1 > h2 else 1 # sic! - smaller rank is stronger

compare_key = cmp_to_key(compare)

all_hands = []      # list of hands to be sorted later
hand_bids = dict()  # bid values referenced by hand

# Collect all hands and bids into all_hands and hand_bids
for s in input_data:
    if len(s) < 2: # skip potential empty lines at end of file 
        continue
    hand, bid = s.split()
    all_hands.append(hand)
    hand_bids[hand] = int(bid)

all_hands.sort(key=compare_key)

p2_sum = 0
for i, h in enumerate(all_hands):
    p2_sum += (i+1) * hand_bids[h]

print("Part 2:", p2_sum) 
