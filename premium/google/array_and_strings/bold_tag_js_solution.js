/**
 * @param {string} s
 * @param {string[]} dict
 * @return {string}
 */
const addBoldTag = (s, dict) => {
  const boldLetter = addFlagToInsertBold(s, dict); 
  const addBold = insertBoldTag(s, boldLetter);
  
  return addBold;
};

const addFlagToInsertBold = (s, dict) => {
  const boldLetter = new Array(s.length);
  
  boldLetter.fill(false);
  
  Object.keys(dict).map(key =>{
    let fromIndex = 0;
    let start = s.indexOf(dict[key], fromIndex);
    
    while (start !== -1) {
      for (let i = 0; i < dict[key].length; i++)
        boldLetter[start + i] = true;
        
        fromIndex = start + 1;
        start = s.indexOf(dict[key], fromIndex);
    }
  });
  return boldLetter
}


const insertBoldTag = (s, boldLetter) =>
  s.split('').reduce((addBold, curr, i, arr) => {
    if (boldLetter[i]) {
      if (i === 0 || !boldLetter[i - 1])
        addBold += '<b>';
      
      addBold += curr;

      if (i === arr.length - 1 || !boldLetter[i + 1])
        addBold += '</b>';
    } else {
      addBold += curr;
    }
    return addBold;
  }, '');
