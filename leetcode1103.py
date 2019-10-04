class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0] * num_people
        a = 0
        count = 0
        while a < num_people:
            count += 1
            if count <= candies:
                res[a] += count
                candies -= count
                a += 1
            else:
                res[a] +=  candies
                candies = 0
            if a == num_people and candies != 0:
                a = 0
            if candies == 0:
                break
        return(res)

if __name__ == '__main__':
    candies, num_people = 10, 3
    s = Solution()
    print(s.distributeCandies(candies, num_people))