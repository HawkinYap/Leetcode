class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        R_index = 0
        count = 0

        for line in board:
            if 'R' in line:
                R_index = line.index('R')
                l = line[:R_index]
                l.reverse()
                r = line[R_index+1:]
                for i in l:
                    if i == 'B':
                        break
                    if i == 'p':
                        count += 1
                        break
                for j in r:
                    if j == 'B':
                        break
                    if j == 'p':
                        count += 1
                        break
        v = [i[R_index] for i in board]
        v_index = v.index('R')
        up = v [:v_index]
        up.reverse()
        down =v [v_index+1:]
        for i in up:
            if i == 'B':
                break
            if i == 'p':
                count += 1
                break
        for j in down:
            if j == 'B':
                break
            if j == 'p':
                count += 1
                break
        return(count)




if __name__ == '__main__':
    board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    s = Solution()
    print(s.numRookCaptures(board))