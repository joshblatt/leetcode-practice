# O(n^2) time O(n^2 space)
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0 for _ in range(3)]
        cols = [0 for _ in range(3)]
        diag = 0 # top left to bottom right
        anti_diag = 0 # top right to bottom left
        player_a_val = 1
        player_b_val = -1
        player_val = 0
        for i in range(len(moves)):
            (row, col) = moves[i]
    
            if i % 2 == 0:
                player_val = player_a_val
            else:
                player_val = player_b_val
            
            rows[row] += player_val
            cols[col] += player_val
            if (row, col) == (0,0) or (row, col) == (1,1) or (row, col) == (2,2):
                diag += player_val
            if (row, col) == (0,2) or (row, col) == (1,1) or (row, col) == (2,0):
                anti_diag += player_val
            
            if any(abs(line) == 3 for line in (rows[row], cols[col], diag, anti_diag)):
                return "A" if player_val == player_a_val else "B"
        return "Draw" if len(moves) == 9 else "Pending"