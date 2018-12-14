//https://leetcode.com/explore/interview/card/google/59/array-and-strings/454/
/**
 * @param {number[]} nums
 * @return {number}
 */
const findMaxConsecutiveOnes = (nums) => {
  let start = 0;
  let res = 0;

  while (start < nums.length) {
    if (nums[start] === 1) {
      let end = start + 1;
      while (end < nums.length && nums[end] === 1) end += 1;
      res = Math.max(res, end - start);
      start = end + 1;
    }
    else start += 1;
  }

  return res;
};

const a = findMaxConsecutiveOnes([1,1,1,1]);
const b = findMaxConsecutiveOnes([0,0,0,0]);
const c = findMaxConsecutiveOnes([0,1,0,1]);
const d = findMaxConsecutiveOnes([1,1,0,1,1,1]); 

console.log(`Expecting 4: ${a}`);
console.log(`Expecting 0: ${b}`);
console.log(`Expecting 1: ${c}`);
console.log(`Expecting 3: ${d}`);
