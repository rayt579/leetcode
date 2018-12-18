/**
 * @param {number[]} nums
 * @return {number}
 */
const firstMissingPositive = (nums) => {
  for (let i = 0; i < nums.length; i++) {
    while (nums[i] > 0 && nums[i] < nums.length && nums[i] != nums[nums[i] - 1]) {
      const tmp = nums[nums[i] - 1];
      nums[nums[i] - 1] = nums[i];
      nums[i] = tmp;
    }
  }

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] != i + 1) return i + 1;
  }

  return nums.length + 1;
}



const res = firstMissingPositive([1,2,0]);
console.log(`Expecting 3: ${res}`);

const res2 = firstMissingPositive([3,4,-1,1]);
console.log(`Expecting 2: ${res2}`);

const res3 = firstMissingPositive([7,8,9,11,12]);
console.log(`Expecting 1: ${res3}`);
