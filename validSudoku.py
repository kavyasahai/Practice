class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            elems = []
            for element in row:
                if (element != "." and element in elems):
                    return False
                elif (element != "."):
                    elems.append(element)

        for col in range(0, 9):
            elems = []
            for row in board:
                if (row[col] != "." and row[col] in elems):
                    return False
                elif (row[col] != "."):
                    elems.append(row[col])

        col = 0
        row = 0

        while (col < 9):
            while (row < 9):
                elems = []
                for i in range(0, 3):
                    for j in range(0, 3):
                        item = board[row + i][col + j]
                        if (item != "." and item in elems):
                            return False
                        elif (item != "."):
                            elems.append(item)
                        # print(row+i," ",col+j," ",board[row+i][col+j])
                row += 3
            col += 3
            row = 0

        return True





