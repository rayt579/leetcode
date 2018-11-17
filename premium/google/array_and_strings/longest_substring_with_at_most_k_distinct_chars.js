/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var lengthOfLongestSubstringKDistinct = function(s, k) {
  return solution(s, k);
};

const solution = function lengthOfLongestSubstringWithAtMostKDistinctCharacters(text, k) {
  let res = 0;
  let start = 0;
  let end = 0;
  let distinctCharacters = new Map();

  if (typeof k !== 'number' || typeof text !== 'string' || k <= 0) return 0;

  while (start < text.length && end < text.length) { 
    let character = text.charAt(end);

    if (distinctCharacters.has(character)) {
      distinctCharacters.set(character, distinctCharacters.get(character) + 1);
    }
    else {
      distinctCharacters.set(character, 1);
    }

    while (start <= end && distinctCharacters.size > k) {
      let character = text.charAt(start);
      distinctCharacters.set(character, distinctCharacters.get(character) - 1);
      if (distinctCharacters.get(character) === 0) {
	distinctCharacters.delete(character);
      }
      
      start += 1;
    }

    end += 1;
    res = Math.max(res, end - start);
  }

  return res;
}

const res = lengthOfLongestSubstringKDistinct('eceba', 2);
console.log(`Expecting 3: ${res}`);

const res2 = lengthOfLongestSubstringKDistinct('aa', 1);
console.log(`Expecting 2: ${res2}`);

const res3 = lengthOfLongestSubstringKDistinct('ab', 1);
console.log(`Expecting 1: ${res3}`);

const res4 = lengthOfLongestSubstringKDistinct('bacc', 2);
console.log(`Expecting 3: ${res4}`);
