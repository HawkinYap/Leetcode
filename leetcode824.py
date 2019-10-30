class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        a = S.split(' ')
        for i, j in enumerate(a):
            tmp = ['m'] + ['a'] * (i + 2)
            if j[0] not in 'aeiouAEIOU': 
                j = j[1:] + j[0]
            a[i] = j + "".join(tmp)

        return(" ".join(a))


if __name__ == "__main__":
    S = "Each word consists of lowercase and uppercase letters only"
    s = Solution()
    print(s.toGoatLatin(S))