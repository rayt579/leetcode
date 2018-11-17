/**
 * @param {string} s
 * @param {string[]} dict
 * @return {string}
 */
var addBoldTag = function(s, dict) {
  return solution(s, dict);
};

const solution = function addBoldTagInText(text, words) {
  const mergeIntervals = function mergeIntervals(intervals) {
    intervals.sort( (i1, i2) => i1.start - i2.start);
    let curr = 1;
    let mergedIntervals = [intervals[0]];

    while (curr < intervals.length) {
      if (intervals[curr].start - 1 <= mergedIntervals[mergedIntervals.length - 1].end) {
	let mergedInterval = new Interval(
	  mergedIntervals[mergedIntervals.length - 1].start, 
	  Math.max(intervals[curr].end, mergedIntervals[mergedIntervals.length - 1].end)
	);

	mergedIntervals.pop();
	mergedIntervals.push(mergedInterval);
      }
      else {
	mergedIntervals.push(intervals[curr]);
      }

      curr += 1;
    }
    
    return mergedIntervals;
  }


  const getSubstringIntervals = function getSubstringIntervals(text, words) {
    let substringIntervals = [];

    for (let substr of words) {
      let substringIndex = text.indexOf(substr);
      while (substringIndex !== -1) {
	substringIntervals.push(new Interval(substringIndex, substringIndex + substr.length - 1));
	substringIndex += 1;
	substringIndex = text.indexOf(substr, substringIndex);
      }
    }

    if (substringIntervals.length === 0) return substringIntervals;

    return mergeIntervals(substringIntervals);
  }
  
  if (typeof(text) !== 'string' || typeof(words) !== 'object') return null;
  if (words.length === 0) return text;

  let substringIntervals = getSubstringIntervals(text, words);
  let OPENTAG = '<b>';
  let CLOSETAG = '</b>';
  let curr = 0;
  let res = [];

  while (curr < text.length) {
    if (substringIntervals.length > 0 && substringIntervals[0].start === curr) {
      res.push(OPENTAG);
      while (curr <= substringIntervals[0].end) {
	res.push(text[curr]);
	curr += 1;
      }
      res.push(CLOSETAG);
      substringIntervals.shift();
    }
    else {
      res.push(text[curr]);
      curr += 1;
    }
  }

  return res.join('');
}

class Interval {
  constructor(start, end) { 
    this.start = start;
    this.end = end;
  }
}

//Driver
res = addBoldTag('abcxyz123', ['abc','123']);
console.log(`Expecting <b>abc</b>xyz<b>123</b> : ${res}`);

res2 = addBoldTag('aaabbcc', ['aaa','aab','bc']);
console.log(`Expecting <b>aaabbc</b>c : ${res2}`);

res3 = addBoldTag('aaabbcc', ['d']);
console.log(`Expecting aaabbcc: ${res3}`);

res4 = addBoldTag('aaabbcc', ['a', 'b', 'c']);
console.log(`Expecting <b>aaabbcc</b>: ${res4}`);
