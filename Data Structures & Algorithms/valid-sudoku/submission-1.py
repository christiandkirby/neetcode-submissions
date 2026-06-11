class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Question(s):
        # What is the data representation?
        # What is the expected Time and Space Complexity
        # Does Time and Space Complexity even matter?
        
        # Brute force is O(N^2) as you can loop through all positions 
        # checking for valid column and row

        # Need to know if the sub 3x3's are valid
        # Need to know if the 9x9 is valid

        # Potential Solution would be to break the board into its 3x3
        # sub boards, check is they are valid, combine then check again
        # if at any point a sub-board returns false, you would return False
        # Otherwise, you'd return True


        # Validate rows
        for i in range(9):
            row_set = set()
            for j in range(9):
                item = board[i][j]
                if item in row_set:
                    return False
                elif item != '.':
                    row_set.add(item)



        # Validate Columns
        for i in range(9):
            col_set = set()
            for j in range(9):
                item = board[j][i]
                if item in col_set:
                    return False
                elif item != '.':
                    col_set.add(item)



        # Validate the 3X3 Sub-Boards
        starts = [(0,0), (0,3), (0,6),
                  (3,0), (3,3), (3,6),
                  (6,0), (6,3), (6,6)]

        for i, j in starts:
            box_set = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in box_set:
                        return False
                    elif item != '.':
                        box_set.add(item)
        return True

        # Time Complexity : O(N^2)
        # Space Complexity : O(N^2)



