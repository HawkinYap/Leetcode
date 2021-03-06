
# class Codec:
#     def __init__(self):
#         self.en_dict = {}
#         self.i = 0

#     def encode(self, longUrl):
#         shortURL = "http://sixkery.top/dream" + str(self.i)
#         self.en_dict[shortURL] = longUrl
#         self.i += 1
#         return shortURL

#     def decode(self, shortUrl):
#         return self.en_dict[shortUrl]
import random
import string

class Codec:

    alphabet = string.ascii_letters + string.digits
    # print(string.ascii_letters)
    
    def __init__(self):
        self.url2code = {}
        self.code2url = {}
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.url2code:
            code = ''.join(random.choice(self.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl[-6:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

if __name__ == "__main__":
    
    longUrl = 'http://speciallan.com/problem535.html'
    # http://tinyurl.com/3k2i1d

    c = Codec()
    shortUrl = c.encode(longUrl)
    longUrl2 = c.decode(shortUrl)

    print(longUrl)
    print(shortUrl)
    print(longUrl)

# if __name__ == '__main__':
#     codec = Codec()
#     print((codec.encode('https://leetcode.com/problems/design-tinyurl')))


