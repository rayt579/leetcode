/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
const moveZeroes = (nums) => {
  let insertIndex = 0
  for (let num of nums) {
    if (num != 0) {
      nums[insertIndex] = num;
      insertIndex += 1;
    }
  }

  for (let i=insertIndex; i < nums.length; i++) {
    nums[i] = 0;
  }
  
  return nums;
};

const moveZeroesInitial = (nums) => {
  let a = 0;
  let b = 1;
  while (a < nums.length && b < nums.length) {
    while (a < nums.length && nums[a] !== 0) a += 1;
    while (b <= a || b < nums.length && nums[b] === 0) b += 1;
    if (a < nums.length && b < nums.length) {
      [ nums[a], nums[b] ] = [ nums[b], nums[a] ];
    }
  }
  
  return nums;
};

const res = moveZeroes([0,1,0,3,12]);
console.log(`expecting [1,3,12,0,0]: ${res}`);

const res2 = moveZeroes([4,2,4,0,0,3,0,5,1,0]);
console.log(`expecting [4,2,4,3,5,1,0,0,0,0]: ${res2}`);

const res3 = moveZeroes([0,0,0,1,2,3]);
console.log(`expecting [1, 2, 3, 0, 0, 0]: ${res3}`);

