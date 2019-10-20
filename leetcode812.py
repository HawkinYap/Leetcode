class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # area = 0
        # for i in range(len(points)-2):
        #     for k in range(i+1, len(points)-1):
        #         for m in range(k+1, len(points)):
        #             x1 = points[i][0]
        #             y1 = points[i][1]
        #             x2 = points[k][0]
        #             y2 = points[k][1]
        #             x3 = points[m][0]
        #             y3 = points[m][1]
        #             area = max(area, abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3)))
        # return(area / 2)

        from itertools import combinations
        amax = 0
        for i in combinations(points, 3):
            x = [i[0][0], i[1][0], i[2][0]]
            y = [i[0][1], i[1][1], i[2][1]]
            s = abs((x[0]-x[2])*(y[1]-y[2])-(x[1]-x[2])*(y[0]-y[2]))/2
            amax=max(s,amax)
        return(amax)


if __name__ == "__main__":
    points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    s = Solution()
    print(s.largestTriangleArea(points))