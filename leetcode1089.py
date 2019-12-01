class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 2
            else:
                i += 1

    

if __name__ == "__main__":
    arr = [1,0,2,3,0,4,5,0]
    s = Solution()
    print(s.duplicateZeros(arr))