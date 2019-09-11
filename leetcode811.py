class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        num = {}
        for domin in cpdomains:
            count = int(domin.split(" ")[0])
            lst = domin.split(" ")[1].split(".")
            for i in range(len(lst)):
                dm = ".".join(lst[i:])
                if dm in num:
                    num[dm] += count
                else:
                    num[dm] = count
        return([str(n)+" "+d for d, n in num.items()])
        

if __name__ == '__main__':
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    s = Solution()
    print(s.subdomainVisits(cpdomains))
