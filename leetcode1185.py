class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        '''
        蔡勒公式 - Zelle
        w = (y+[y/4]+[c/4]-2c+[26(m+1)/10]+d-1) mod 7
        w：星期（计算所得的数值对应的星期：0-星期日；1-星期一；2-星期二；3-星期三；4-星期四；5-星期五；6-星期六）[1]
        c：年份前两位数
        y：年份后两位数
        m：月（m的取值范围为3至14，即在蔡勒公式中，某年的1、2月要看作上一年的13、14月来计算，比如2003年1月1日要看作2002年的13月1日来计算）
        d：日
        []:向下取整
        '''
        y = int(str(year)[-2:])
        c = int(str(year)[:2])
        result = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if month < 3 :
            y -= 1
            month += 12
        i = (y + y // 4 + c // 4 - 2*c + (26 * (month + 1) // 10) + day - 1) % 7
        return result[i]

if __name__ == "__main__":
    day, month, year = 18, 7, 1999
    s = Solution()
    print(s.dayOfTheWeek(day, month, year))

