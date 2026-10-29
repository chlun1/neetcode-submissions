class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        n_groups = len(hand) // groupSize
        hand.sort()
        used = set()

        for gp in range(n_groups):
            curr_sz = 0
            prev = None

            for i in range(len(hand)):
                if i in used:
                    continue
                if hand[i] == prev:
                    continue
                if prev is not None and hand[i] - prev != 1:
                    return False

                used.add(i)
                prev = hand[i]
                curr_sz += 1

                if curr_sz == groupSize:
                    break
            
            if curr_sz != groupSize:
                return False

        return True
        