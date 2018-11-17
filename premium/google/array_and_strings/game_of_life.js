/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
const countLiveNeighborsAt = (board, x, y) => {
}

const gameOfLife = board => {
  if (typeof(board) === 'undefined' || board.length === 0) return;

  let m = board.length;
  let n = board[0].length;

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      let liveNeighbors = countLiveNeighborsAt(board, i, j);
      
      if (board[i][j] === 0) {
	if (liveNeighbors === 3)
	  board[i][j] = 2;
      }
      else {
	if (liveNeighbors !== 2 && liveNeighbors !== 3) {
	  board[i][j] = 3;
	}
      }
    }
  }

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] !== 1) {
	board[i][j] >>= 1;
      }
    }
  }
};
