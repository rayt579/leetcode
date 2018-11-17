/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
  const R = 10;
  let carry = 1;
  let res = [];

  for (let i = digits.length - 1; i >= 0; i--) {
    const digit = (digits[i] + carry) % R;
    carry = (digits[i] !== 0 && digit === 0) ? 1 : 0;
    res.unshift(digit);
  }

  if (carry === 1) {
    res.unshift(1); 
  }

  return res;
}

const a = plusOne([1,2,3])
console.log(`Expecting [1,2,4] : ${a}`);

const b = plusOne([1,2,9]);
console.log(`Expecting [1,3,0] : ${b}`);

const c = plusOne([9,9,9]);
console.log(`Expecting [1,0,0,0] : ${c}`);
