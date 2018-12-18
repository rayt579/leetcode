/**
 * @param {string} s
 * @return {number}
 */
const firstUniqChar = (s) => {
  if (typeof(s) !== 'string') return -1;
  let counts = new Map();
  for (let c of s) {
    if (!counts.has(c)) counts.set(c, 1);
    else counts.set(c, counts.get(c) + 1);
  }

  for (let i = 0; i < s.length; i++) {
    if (counts.get(s[i]) === 1) return i;
  }

  return -1;
};

const res = firstUniqChar('leetcode');
console.log(`Expect 0: ${res}`);

const res2 = firstUniqChar('loveleetcode');
console.log(`Expect 2: ${res2}`);
