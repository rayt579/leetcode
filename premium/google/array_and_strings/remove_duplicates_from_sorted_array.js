/**
https://leetcode.com/explore/interview/card/google/59/array-and-strings/464/
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
const removeDuplicatesUsingSwaps = (nums) => { 
  let i = 0;
  let j = 0;
  while (j < nums.length) {
    [ nums[i], nums[j] ] = [ nums[j], nums[i] ];
    j += 1;
    while (j < nums.length && nums[i] === nums[j]) j += 1;
    i += 1
  }

  return i;
};

const removeDuplicates = (nums) => {
  let i = 0; 
  for (let j = 1; j < nums.length; j++) {
    if (nums[i] !== nums[j]) {
      i += 1;
      nums[i] = nums[j];
    }
  }

  return i + 1;
};

console.log(`Expecting 2: ${removeDuplicates([1,1,2])}`);
console.log(`Expecting 5: ${removeDuplicates([0,0,1,1,1,2,2,3,3,4])}`);
console.log(`Expecting 5: ${removeDuplicates([1,2,3,4,5])}`);
console.log(`Expecting 1: ${removeDuplicates([1,1,1,1,1])}`);
