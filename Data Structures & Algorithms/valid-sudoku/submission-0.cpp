class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for(int i = 0; i < 9; i++) {
            unordered_set<char> seen;
            for(int j = 0; j < 9; j++) {
                if (board[i][j] == '.') continue;
                if (seen.count(board[i][j])) {
                    return false;
                }
                seen.insert(board[i][j]);
            }
        }
        for(int i = 0; i < 9; i++) {
            unordered_set<char> seen;
            for(int j = 0; j < 9; j++) {
                if (board[j][i] == '.') continue;
                if (seen.count(board[j][i])) {
                    return false;
                }
                seen.insert(board[j][i]);
            }
        }
        for(int i = 0; i < 9; i++) {
            unordered_set<char> seen;
            int x = i / 3;
            x = x * 3;
            int y = (i % 3) * 3;
            for(int j = 0; j < 9; j++) {
                int r = x + (j / 3);
                int c = y + (j % 3);
                if (board[r][c] == '.') continue;
                if (seen.count(board[r][c])) {
                    return false;
                }
                seen.insert(board[r][c]);
            }
        }
        return true;
    }
};
