//https://leetcode.com/explore/interview/card/google/59/array-and-strings/455/
/**
 * @param {number[]} nums
 * @return {number}
 */
const findMaxConsecutiveOnesGreedy = (nums) => {
  let prev = 0;
  let localMaxConsecutiveOnes = 0;
  let globalMaxConsecutiveOnes = 0;
  

  for (let num of nums) {
    if (num === 1) {
      localMaxConsecutiveOnes += 1;
      prev += 1;
    }
    else {
      localMaxConsecutiveOnes = prev + 1;
      prev = 0;
    }

    globalMaxConsecutiveOnes = Math.max(globalMaxConsecutiveOnes, localMaxConsecutiveOnes);
  }
};


const findMaxConsecutiveOnes = (nums) => {
  let maxConsecutiveOnes = 0;
  let zeroCounts = 0;
  const k = 1;
  let start = 0;
  for (let end = 0; end < nums.length; end++) {
    if (nums[end] === 0) zeroCounts += 1;

    while (zeroCounts > k) {
      if (nums[start] === 0) zeroCounts -= 1;
      start += 1;
    }

    maxConsecutiveOnes = Math.max(maxConsecutiveOnes, end - start + 1);
  }

  return maxConsecutiveOnes;
};

const a = findMaxConsecutiveOnes([1,0,1,0,1,1,1]);
const b = findMaxConsecutiveOnes([1,0,1,1,0]);
const c = findMaxConsecutiveOnes([1,1,1,1,1]);
const d = findMaxConsecutiveOnes([0, 0, 0, 0]);

console.log(`Expecting result 5: ${a}`);
console.log(`expecting result 4: ${b}`);
console.log(`expecting result 5: ${c}`);
console.log(`expecting result 1: ${d}`);
