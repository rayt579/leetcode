/**
 * @param {number[][]} M
 * @return {number[][]}
 */
const imageSmoother = (M) => {
  if (M === undefined) return undefined;

  const numRows = M.length;
  const numCols = M[0].length;

  for (let i = 0; i < numRows; i++) {
    for (let j = 0; j < numCols; j++) {
      let total = 0;
      let count = 0;

      for (let x = i - 1; x <= i + 1; x++) {
	for (let y = j - 1; y <= j + 1; y++) {
	  if (x >= 0 && x < numRows && y >= 0 && y < numCols) {
	    total = total + (M[x][y] & 0xFF);
	    count += 1;
	  }
	}
      }

      M[i][j] = Math.floor(total / count) << 8 | M[i][j];
    }
  }

  for (let i = 0; i < numRows; i++) {
    for (let j = 0; j < numCols; j++) {
	M[i][j] = M[i][j] >> 8;
    }
  }

  return M;
};


const res = imageSmoother([[1,1,1],[1,0,1],[1,1,1]]);
console.log(res);
