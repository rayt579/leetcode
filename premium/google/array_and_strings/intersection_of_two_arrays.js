//https://leetcode.com/problems/intersection-of-two-arrays/
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
const intersection = (nums1, nums2) => {
  if (typeof(nums1) === 'undefined' || typeof(nums2) === 'undefined') return undefined;
  
  let intersections = new Map();
  let res = [];

  nums1.forEach(n => {
    if (!intersections.has(n)) intersections.set(n, false)
  });

  nums2.forEach(n => {
    if (intersections.has(n) && intersections.get(n) == false) {
      res.push(n);
      intersections.set(n, true);
    }
  });

  return res;
};

const res = intersection([1,2,2,1],[2,2]);
console.log(`Expecting {2}: ${res}`);
