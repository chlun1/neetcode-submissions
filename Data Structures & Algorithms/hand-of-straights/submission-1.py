from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)
        hand.sort()

        for first in hand:
            if counts[first] > 0:
                for num in range(first, first + groupSize):
                    if counts[num] == 0:
                        return False

                    counts[num] -= 1

        return True
        