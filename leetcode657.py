class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # vertical = 0
        # horizontal = 0
        # for move in moves:
        #     if move == 'U':
        #         vertical += 1
        #     if move == 'D':
        #         vertical -= 1
        #     if move == 'L':
        #         horizontal += 1
        #     if move == 'R':
        #         horizontal -= 1
        # if vertical == 0 and horizontal == 0:
        #     return(True)
        # else:
        #     return(False)

        if moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R'):
             return True
        return False


if __name__ == '__main__':
    moves = 'LL'
    solution = Solution()
    print(solution.judgeCircle(moves))