//https://leetcode.com/explore/interview/card/google/59/array-and-strings/443/
/**
 * @param {string} s
 * @return {boolean}
 */
const isNumber = (s) => {
  if (typeof(s) !== 'string') return false;
  s = s.trim();

  let digitSeen = false;
  let eSeen = false;
  let pointSeen = false;

  for (let i = 0; i < s.length; i++) {
    if (s[i] >= '0' && s[i] <= '9') {
      digitSeen = true;
    }
    else if (s[i] === '.') {
      if (pointSeen || eSeen) return false;
      pointSeen = true;
    }
    else if (s[i] === 'e') {
      if (eSeen || !digitSeen) return false;
      eSeen = true;
      digitSeen = false;
    }
    else if (s[i] === '+' || s[i] === '-') {
      if (i !== 0 && s[i-1] !== 'e') return false;
    }
    else return false;
  }

  return digitSeen;
};

res = isNumber('-4.75e+4');
console.log(`Expecting true: ${res}`);
res2 = isNumber('-4.755345e');
console.log(`Expecting false: ${res2}`);
