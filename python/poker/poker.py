def best_hands(hands):
    """Takes the list and return the best hand.

    Parameter:
        hands (list): All the given hands.

    Returns:
        list: The best hand.
    """

    hands_category = {}

    for hand in hands:
        category = 0

        current_hand = hand.split(" ")
        current_rank = []
        suits = []

        for current in current_hand:
            current_rank.append(current[:-1])
            suits.append(current[-1])

        hash_map = {
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14
        }

        for i in range(len(current_rank)):
            if current_rank[i].isnumeric():
                current_rank[i] = int(current_rank[i])
            else:
                current_rank[i] = hash_map[current_rank[i]]

        current_rank = sorted(current_rank, reverse=True)

        rank_counter = {}

        for num in current_rank:
            if num in rank_counter:
                rank_counter[num] += 1
            else:
                rank_counter[num] = 1

        flush = False
        if len(set(suits)) == 1:
            flush = True

        straight = True

        for i in range(len(current_rank) - 1):
            if current_rank[i] != current_rank[i + 1] + 1:
                straight = False
                break

        if current_rank == [14, 5, 4, 3, 2]:
            straight = True

        straight_flush = False

        if straight and flush:
            straight_flush = True

        if straight_flush:
            category = 8

        elif 4 in rank_counter.values():
            category = 7

        elif 3 in rank_counter.values() and 2 in rank_counter.values():
            category = 6

        elif flush:
            category = 5

        elif straight:
            category = 4

        elif 3 in rank_counter.values():
            category = 3

        elif list(rank_counter.values()).count(2) == 2:
            category = 2

        elif 2 in rank_counter.values():
            category = 1

        hands_category[hand] = category

    max_value = max(hands_category.values())

    final_cat = []
    for cat in hands_category:
        if hands_category[cat] == max_value:
            final_cat.append(cat)