import time
class Solution(object):
    def countNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = 0
        b = set(s)
        for i in b:
            d = s.count(i)
            if d != 1:
                c += 1
        return(len(set(s)) + c)
        # ch_num_dict = {}
        # for ch in s:
        #     if ch in ch_num_dict:
        #         ch_num_dict[ch] += 1
        #     else:
        #         ch_num_dict[ch] = 1

        # result = 0
        # for k, v in ch_num_dict.items():
        #     if v == 1:
        #         result += 1
        #     else:
        #         result += (1 + v)

        # return(result)

        
        
if __name__ == '__main__':
    time_start=time.clock() 
    s = ['a', 'a', 'b', 'b', 'e', 'e', 'e']
    solution = Solution()
    print(solution.countNumber(s))
    time_end=time.clock()
    print('totally cost',time_end-time_start)