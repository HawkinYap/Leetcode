from bisect import bisect_left as locate
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # while len(stones) > 1:
        #     stones.sort()
        #     stones.reverse()
        #     stones[0], stones[1] = stones[0]-stones[1], 0
        #     stones.pop(1)
        # if stones[0] == 0:
        #     return(0)
        # else:
        #     return(stones[0])
        stones.sort()
        while len(stones) > 1:
            stone_1, stone_2 = stones.pop(), stones.pop()
            if stone_1 != stone_2:
                stone_rest = stone_1 - stone_2
                stones.insert(locate(stones, stone_rest), stone_rest)
        return stones[0] if len(stones) > 0 else 0



if __name__ == "__main__":
    stones = [5, 8, 6, 3]
    s = Solution()
    print(s.lastStoneWeight(stones))