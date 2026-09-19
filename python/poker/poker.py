def best_hands(hands):
    """Takes the list and return the best hand.

    Parameter:
        hands(list): All the given hands.
    
    returns:
        list: The best hand
    """

    for hand in hands:
        current_hand = hand.split(" ")
        current_rank = []
        suits = []
        for current in current_hand:
            current_rank.append(current[:-1])
            suits.append(current[-1])

        hash_map = {
            "J" : 11,
            "Q" : 12,
            "K" : 13,
            "A" : 14
        }

        for i in range(len(current_rank)):
            if current_rank[i].isnumeric():
                current_rank[i] = int(current_rank[i])
            else:
                current_rank[i] = hash_map[current_rank[i]]

        current_rank = sorted(current_rank , reverse=True)

        rank_counter = {}

        for num in current_rank:
            if num in rank_counter:
                rank_counter[num] +=  1
            else:
                rank_counter[num] = 1

        if set(suits) == 1:
            pass

        straight = True
        
        for i in range(len(current_rank)-1):
            if current_rank[i] != current_rank[i+1] + 1:
                straight = False
                break

        if current_rank == [14, 5, 4, 3, 2]:
            straight = True
            