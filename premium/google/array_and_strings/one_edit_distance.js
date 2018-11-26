/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const isOneEditDistance = (s, t) => {
  if (s === t) return false;
  if (Math.abs(s.length - t.length) > 1) return false;

  let i = 0;
  let j = 0;
  let edited = false;

  while (i < s.length && j < t.length) {
    if (s[i] !== t[j]) {
      if (edited) return false;
      if (s.length === t.length) {
	i += 1;
	j += 1;
      }
      else if (s.length > t.length) {
	i += 1;
      }
      else {
	j += 1
      }

      edited = true;
    }
    else {
      i += 1;
      j += 1;
    }
  }

  return true;

};

res = isOneEditDistance('ab','acb');
console.log(`Expecting true: ${res}`);

res2 = isOneEditDistance('cab','ad');
console.log(`Expecting false: ${res2}`);

res3 = isOneEditDistance('1203','1213');
console.log(`Expecting true: ${res3}`);

res4 = isOneEditDistance('','');
console.log(`Expecting false: ${res4}`);

res5 = isOneEditDistance('c','c');
console.log(`Expecting false: ${res5}`);

res6 = isOneEditDistance('a','');
console.log(`Expecting true: ${res6}`);

res7 = isOneEditDistance('a','ac');
console.log(`Expecting true: ${res7}`);
