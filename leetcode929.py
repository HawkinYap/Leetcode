import re

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        mail_list = []
        for email in emails:
            email_ = re.sub(r"\+.*?@", "@", email)
            s = email_.split("@")
            a = s[0].replace(".", "") + "@" + s[1]
            if a not in mail_list:
                mail_list.append(a)
        
        return(len(mail_list))



if __name__ == '__main__':
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    s = Solution()
    print(s.numUniqueEmails(emails))