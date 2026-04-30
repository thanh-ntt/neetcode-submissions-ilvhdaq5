class Solution {
    public void solve(char[][] board) {
        for (int i = 0; i < board.length; i++) {
            // System.out.println(Arrays.toString(board[i]));
        }
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                // System.out.println("New stack " + i + ", " + j);
                boolean edge = false;
                Stack<int[]> s = new Stack<>();
                List<int[]> list = new ArrayList<>();
                s.push(new int[]{i, j});
                while (!s.isEmpty()) {
                    int[] pos = s.pop();
                    // System.out.println("pop " + pos[0] + ", " + pos[1] + " -> " + board[pos[0]][pos[1]]);
                    if (pos[0] < 0 || pos[0] >= board.length || pos[1] < 0 || pos[1] >= board[0].length) {
                        // System.out.println("Invalid" + Arrays.toString(pos));
                    }
                    if (board[pos[0]][pos[1]] == 'X' || board[pos[0]][pos[1]] == 'I') continue;
                    list.add(pos);
                    board[pos[0]][pos[1]] = 'I';
                    if (pos[0] == 0) edge = true;
                    else s.push(new int[]{pos[0] - 1, pos[1]});
                    if (pos[0] == board.length - 1) edge = true;
                    else s.push(new int[]{pos[0] + 1, pos[1]});
                    if (pos[1] == 0) edge = true;
                    else s.push(new int[]{pos[0], pos[1] - 1});
                    if (pos[1] == board[0].length - 1) edge = true;
                    else s.push(new int[]{pos[0], pos[1] + 1});
                }
                // if (!list.isEmpty()) System.out.println("Edge: " + edge);
                if (!edge) {
                    for (int[] pos : list) {
                        board[pos[0]][pos[1]] = 'X';
                    }
                }
            }
        }
        for (int i = 0; i < board.length; i++) {
            // System.out.println(Arrays.toString(board[i]));
        }
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == 'I') board[i][j] = 'O';
            }
        }
    }
}
/*
["O","X","X","O","X"]
["X","O","O","X","O"]
["X","O","X","O","X"]
["O","X","O","O","O"]
["X","X","O","X","O"]

["O","X","X","O","X"]
["X","X","X","X","O"]
["X","X","X","X","X"]
["O","X","O","X","O"]
["X","X","X","X","X"]
*/
