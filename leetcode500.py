class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # res = []
        # keys = ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM']
        # for word in words:
        #     for key in keys:
        #         word_upper = word.upper()
        #         if set(word_upper) <= set(key):
        #             res.append(word)
        # return(res)

        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        res = []
        for i in words:
            x = i.lower()
            setx = set(x)
            if setx<=set1 or setx<=set2 or setx<=set3:
                res.append(i)
        return(res)


if __name__ == '__main__':
    words = ["asdfghjkl","qwertyuiop","zxcvbnm"]
    s = Solution()
    print(s.findWords(words))