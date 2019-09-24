class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        wordsLen = 0
        dct = {}
        charsSet = set(chars)
        for c in charsSet:
            dct[c]=chars.count(c)
        
        for word in words:
            flag =1
            for i in range(len(word)):
                if word[i] not in chars:
                    flag=0
                    break
            if flag==1:
                wordSet = set(word)
                flag2 = 1
                for w in wordSet:
                    if word.count(w)>dct[w]:
                        flag2=0
                        break
                if flag2==1:
                    wordsLen+=len(word)
                    
        return(wordsLen)

if __name__ == '__main__':
    words = ["cat","bt","hat","tree"]
    chars = 'atach'
    s = Solution()
    print(s.countCharacters(words, chars))