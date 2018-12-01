/**
 * @param {string} s
 * @return {boolean}
 */
const isNumber = (s) => {
  if (typeof(s) !== 'string') return false;
  s = s.trim();
  const validStates = [1,5,6];
  const dfa = [
    {'d' : 1, 's' : 2, '.' : 3},
    {'d' : 1, 'e' : 4, '.' : 5},
    {'d' : 1, '.' : 3},
    {'d' : 5},
    {'d' : 6, 's' : 7},
    {'d' : 5, 'e' : 4},
    {'d' : 6},
    {'d' : 6}
  ];

  let currState = 0;
  for (let c of s) {
    const dfaKey = convertToDfaKey(c);
    if (dfa[currState].hasOwnProperty(dfaKey)){
      currState = dfa[currState][dfaKey];
    }
    else
      return false;
  }
  
  return validStates.includes(currState);
};

const convertToDfaKey = (c) => {
  if (c >= '0' && c <= '9') return 'd';
  else if (c === '+' || c === '-') return 's';
  else if (c === 'e'|| c === '.') return c;
  else return 'not a key';
}

console.log(`Expecting true: ${isNumber('-4e+4')}`);
console.log(`Expecting false: ${isNumber('-4e+4.0')}`);
console.log(`Expecting true: ${isNumber('3.')}`);
