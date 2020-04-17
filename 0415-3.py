class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # maxl = 0

        # if not len(s):
        #     return 0
        
        # elif len(s) == 1:
        #     return 1
        # else:
        #     for i in range(len(s) - 1):
        #         lst = [s[i]]  
        #         curl = 1        
        #         for j in range(i+1, len(s)):
        #             if s[j] not in lst:
        #                 lst.append(s[j])
        #                 curl += 1
        #             else:
        #                 break
        #         # print(lst)
        #         # print(curl)
        #         maxl = curl if maxl < curl else maxl

        #     return maxl
        resl = 0
        curl = 0
        lst = []
        for i in range(len(s)):
            if s[i] not in lst:
                lst.append(s[i])
            else:
                curl = len(lst)
                resl = curl if curl > resl else resl
                index = lst.index(s[i])
                lst = lst[index+1:] + [s[i]]

        curl = len(lst)
        resl = curl if curl > resl else resl
        return resl


if __name__ == "__main__":
    s = "abcabcbb"
    slt = Solution()
    print(slt.lengthOfLongestSubstring(s))