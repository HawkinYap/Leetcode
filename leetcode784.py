class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        # res = [S]
        # flag = 0
        # for i in range(len(S)):
        #     if (ord(S[i]) >= 65 and ord(S[i]) <= 90):
        #         flag = 1
        #         tmp = chr(ord(S[i]) + 32)
        #         res.append(S[:i] + tmp + S[i+1:])
        #     if (ord(S[i]) >= 97 and ord(S[i]) <= 122):
        #         flag = 1
        #         tmp = chr(ord(S[i]) - 32)
        #         res.append(S[:i] + tmp + S[i+1:])
        # if flag == 1:
        #     res.append(S.upper())
        #     res.append(S.lower())
        # return(list(set(res)))

        # if not S: return [S]
        # rest = self.letterCasePermutation(S[1:])
        # if S[0].isalpha():
        #     return [S[0].lower() + s for s in rest] + [S[0].upper() + s for s in rest]
        # return [S[0] + s for s in rest]
        
        # res = list()
        # l = len(S)
        # if l == 0:
        #     return [""]
            
        # def dfs(start, temp):
        #     if start >= l or len(temp) == l: #出口
        #         res.append(temp)
        #         return
        #     if S[start].isdigit(): 
        #         dfs(start + 1, temp + S[start])
            
        #     elif S[start].islower(): 
        #         dfs(start + 1, temp + S[start])
        #         dfs(start + 1, temp + S[start].upper())

        #     elif S[start].isupper():
        #         dfs(start + 1, temp + S[start])
        #         dfs(start + 1, temp + S[start].lower())
        
        # dfs(0, "")
        # return(res)

        res=[S]
        for i in range(len(S)):
            if S[i].isdigit():
                continue
            elif S[i].islower():
                res.extend([a[:i]+a[i].upper()+a[i+1:] for a in res])
            else:
                res.extend([a[:i]+a[i].lower()+a[i+1:] for a in res])
        return res
                
                

if __name__ == '__main__':
    S = "a1b2"
    s = Solution()
    print(s.letterCasePermutation(S))