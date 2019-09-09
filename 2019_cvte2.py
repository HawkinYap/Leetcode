import time
class Solution(object):
    def countNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # for i in range(len(s)):
        #     if s.count(s[i]) == 1:
        #         return(i)

        # return([i for i in range(len(s)) if s.count(s[i]) == 1][0])
        ch_num_dict = {}
        for ch in s:
            if ch in ch_num_dict:
                ch_num_dict[ch] += 1
            else:
                ch_num_dict[ch] = 1
        for i, ch in enumerate(s):
            if ch_num_dict[ch] == 1:
                print(i)
                break
        else:
            print(-1)


        
        
if __name__ == '__main__':
    time_start=time.clock() 
    s = "happyhacker"
    solution = Solution()
    print(solution.countNumber(s))
    time_end=time.clock()
    print('totally cost',time_end-time_start)