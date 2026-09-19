def best_hands(hands):
    """Takes the list and returns the best hand.

    Parameters:
        hands (list): All the given hands.

    Returns:
        list: The best hand.
    """

    hand_scores = {}

    for hand in hands:
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

        flush = len(set(suits)) == 1

        straight = True

        for i in range(len(current_rank) - 1):
            if current_rank[i] != current_rank[i + 1] + 1:
                straight = False
                break

        if current_rank == [14, 5, 4, 3, 2]:
            straight = True

        straight_flush = straight and flush

        if straight_flush:
            if current_rank == [14, 5, 4, 3, 2]:
                score = (8, 5)
            else:
                score = (8, current_rank[0])

        elif 4 in rank_counter.values():
            four = max(
                rank for rank in rank_counter
                if rank_counter[rank] == 4
            )
            kicker = max(
                rank for rank in rank_counter
                if rank_counter[rank] == 1
            )
            score = (7, four, kicker)

        elif 3 in rank_counter.values() and 2 in rank_counter.values():
            three = max(
                rank for rank in rank_counter
                if rank_counter[rank] == 3
            )
            pair = max(
                rank for rank in rank_counter
                if rank_counter[rank] == 2
            )
            score = (6, three, pair)

        elif flush:
            score = (5, *current_rank)

        elif straight:
            if current_rank == [14, 5, 4, 3, 2]:
                score = (4, 5)
            else:
                score = (4, current_rank[0])

        elif 3 in rank_counter.values():
            three = max(
                rank for rank in rank_counter
                if rank_counter[rank] == 3
            )
            kickers = sorted(
                [rank for rank in current_rank if rank != three],
                reverse=True
            )
            score = (3, three, *kickers)

        elif list(rank_counter.values()).count(2) == 2:
            pairs = sorted(
                [rank for rank in rank_counter
                 if rank_counter[rank] == 2],
                reverse=True
            )
            kicker = max(
                rank for rank in rank_counter
                if rank_counter[rank] == 1
            )
            score = (2, *pairs, kicker)

        elif 2 in rank_counter.values():
            pair = max(
                rank for rank in rank_counter
                if rank_counter[rank] == 2
            )
            kickers = sorted(
                [rank for rank in current_rank if rank != pair],
                reverse=True
            )
            score = (1, pair, *kickers)

        else:
            score = (0, *current_rank)

        hand_scores[hand] = score

    best_score = max(hand_scores.values())

    return [
        hand
        for hand in hands
        if hand_scores[hand] == best_score
    ]