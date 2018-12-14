/**
 * @param {string} s
 * @return {string}
 */
const shortestPalindrome = (s) => {
  const reverse = [...s].reverse();
  const text = [...s, '#', ...reverse];

  const prefixTable = constructPrefixTable(text);
  const j = prefixTable[prefixTable.length - 1];
  const charsToAdd = [...s.substring(j)].reverse();
  
  return [...charsToAdd, ...s].join('');
};

const constructPrefixTable = (pattern) => {
  let prefixTable = Array(pattern.length).fill(0);
  let j = 0; 
  let i = 1;
  while (j < i && i < pattern.length) {
    if (pattern[i] === pattern[j]) {
      prefixTable[i] = j + 1;
      i += 1;
      j += 1;
    }
    else {
      if (j === 0) i += 1;
      else j = prefixTable[j - 1];
    }
  }

  return prefixTable;
}

const substringSearch = (text, pattern) => {
  const prefixTable = constructPrefixTable(pattern);
  let i = 0;
  let j = 0;
  while (i < text.length && j < pattern.length) {
    while (i < text.length && j < pattern.length && text[i] === pattern[j]) {
      	console.log(`Match at i:${i} j:${j}`);
    	i += 1;
    	j += 1;
    }
    if (j === pattern.length) return true;
    else {
      if (j === 0) i += 1;
      else j = prefixTable[j - 1];
    }
  }

  return false;
}


const res = shortestPalindrome('abc'); 
console.log(res);
