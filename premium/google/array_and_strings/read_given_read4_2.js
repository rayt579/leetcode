//https://leetcode.com/explore/interview/card/google/59/array-and-strings/436/
/**
 * Definition for read4()
 * 
 * @param {character[]} buf Destination buffer
 * @return {number} The number of characters read
 * read4 = function(buf) {
 *     ...
 * };
 */

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
    let readBuffer = [];
    let readIndex = 0;
    let readCount = 0;

    return function(buf, n) {
      let start = 0;
      while (start < n) {
	if (readIndex === 0) readCount = read4(readBuffer);
	if (readCount === 0) break;

	while (start < n && readIndex < readCount) {
	  buf[start] = readBuffer[readIndex];
	  start += 1;
	  readIndex += 1;
	}

	if (readIndex >= readCount) readIndex = 0;
      }

      return start;
    };
};
