//https://leetcode.com/problems/read-n-characters-given-read4/
/**
 * @param {function} read4()
 * @return {function}
 */
var solution = function(read4) {
    /**
     * @param {character[]} buf Destination buffer
     * @param {number} n Maximum number of characters to read
     * @return {number} The number of characters read
     */
    return function(buf, n) {
      let start = 0;
      let readBuffer = ['','','',''];
      
      while (start < n) {
	let readIndex = 0; 

	const readCount = read4(readBuffer);
	if (readCount === 0) break;

	while (start < n && readIndex < readCount) {
	  buf[start] = readBuffer[readIndex];
	  start += 1;
	  readIndex += 1;
	}
      }

      return start;
    };
};
