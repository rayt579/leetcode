//https://leetcode.com/explore/interview/card/google/59/array-and-strings/467/
/**
 * @param {string} s
 * @return {boolean}
 */
const isValid = (s) => {
  const pairs = {'{' : '}', '[':']', '(':')'}
  let stack = [];
  for (let c of s) {
    if (pairs.hasOwnProperty(c)) {
      stack.push(c);
    }
    else {
      if (stack.length === 0) return false;
      const open_paren = stack[stack.length - 1];
      if (c !== pairs[open_paren]) return false;
      stack.pop();
    }
  }

  return stack.length === 0;
};

console.log(`expecting true: ${isValid('[[{()}]]')}`);
console.log(`expecting false: ${isValid('[[{(}]]')}`);
console.log(`expecting false: ${isValid('[[[[[[[[')}`);
console.log(`expecting false: ${isValid(']]]]]]]]')}`);
