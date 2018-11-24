/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
const countLiveNeighborsAt = (board, x, y) => {
  let liveNeighborCount = 0;
  let m = board.length;
  let n = board[0].length;
  const directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]];

  for (const [i, j] of directions) {
    const next_i = i + x;
    const next_j = j + y;

    if (next_i >= 0 && next_i < m && next_j >= 0 && next_j < n) {
      if (board[next_i][next_j] === 2 || board[next_i][next_j] === 3) {
	liveNeighborCount += board[next_i][next_j] & 1;
      }
      else liveNeighborCount += board[next_i][next_j];
    }
  }

  return liveNeighborCount;
}

const gameOfLife = board => {
  if (typeof(board) === 'undefined' || board.length === 0) return;

  const m = board.length;
  const n = board[0].length;

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      const liveNeighbors = countLiveNeighborsAt(board, i, j);
      
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
      if (board[i][j] !== 0 && board[i][j] !== 1) {
	const res = ((board[i][j] & 1) ^ 1);
	board[i][j] = res;
      }
    }
  }
};

let board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]];
gameOfLife(board);
console.log(board);
