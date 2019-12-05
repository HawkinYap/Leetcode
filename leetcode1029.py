class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # sort with costs[i][0] - costs[i][1], the top-k go to A, the other go to B
        return sum((p[0] for i, p in enumerate(sorted(costs, key=lambda x: x[0] - x[1])) if i < len(costs) // 2)) + sum((p[1] for i, p in enumerate(sorted(costs, key=lambda x: x[0] - x[1])) if i >= len(costs) // 2))


if __name__ == "__main__":
    costs = [[10,20],[30,200],[400,50],[30,20]]
    s = Solution()
    s.twoCitySchedCost(costs)