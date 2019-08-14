
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        password = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        trans = []
        for word in words:
            tmp = []
            for i in word:
                tmp.append(password[ord(i)-97])
            trans.append("".join(tmp))
        return(len(set(trans)))
        
                

if __name__ == '__main__':
    words = ["gin", "zen", "gig", "msg"]
    solution = Solution()
    print(solution.uniqueMorseRepresentations(words))