class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # if not rotateArray:
        #     return 0
        # return sorted(rotateArray)[0]
        # if not rotateArray:
        #     return 0

        # for i in range(len(rotateArray) - 1):
        #     if rotateArray[i] > rotateArray[i+1]:
        #         return rotateArray[i+1]
        # return rotateArray[0]

        if not rotateArray:
            return 0

        l = 0
        r = len(rotateArray) - 1
        while l < r:
            mid = (l+r) / 2
            if rotateArray[mid] > rotateArray[r]:
                l = mid + 1
            else:
                r = mid
        return rotateArray[l]


if __name__ == "__main__":
    rotateArray = [3, 4, 5, 1, 2]
    s = Solution()
    print(s.minNumberInRotateArray(rotateArray))