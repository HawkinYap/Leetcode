from collections import Counter

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        # A=[i.lower() for i in licensePlate if i.isalpha()]
        # B=words[:]
        # for i in B:
        #     C=[j for j in i]
        #     for j in A:
        #         if j in C:
        #             C.remove(j)
        #             continue
        #         else:
        #             words.remove(i)
        #             break
        # x=20
        # for i in range(len(words)):
        #     if len(words[i])<x:
        #         x=len(words[i])
        #         b=i
        # print(words)
        # return words[b]

        licensePlate = Counter(filter(str.isalpha, licensePlate.lower()))
        return min(filter(lambda w: not (licensePlate - Counter(w.lower())), words), key=len)




if __name__ == "__main__":
    licensePlate = "1s3 PSt"
    words = ["step","steps","stripe","stepple"]
    s = Solution()
    print(s.shortestCompletingWord(licensePlate, words))