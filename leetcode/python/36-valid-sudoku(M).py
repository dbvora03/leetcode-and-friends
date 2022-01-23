class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            
        rows={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
        cols={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
        grids={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
   
        for row in range(9):
            for col in range(9):
                
                value = board[row][col]
                
                if value == ".":
                    continue
                
                if value in rows[row] or value in cols[col]:
                    return False
                else:
                    rows[row].append(value)
                    cols[col].append(value)
                
                box = (row // 3) * 3 + (col // 3)
                
                if value in grids[box]:
                    return False
                else:
                    grids[box].append(value)
        
        return True