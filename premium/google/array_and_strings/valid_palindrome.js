/**
 * @param {string} s
 * @return {boolean}
 */
const isPalindrome = (s) => {
  const text = s.replace(/[^A-Za-z0-9]/g, '').toLowerCase();
  return isPalindromeIterative(text);
};

const isPalindromeRecursive = (text, start, end) => {
  if (start <= end) return true;
  if (text[start] !== text[end]) return false;
  return isPalindromeRecursive(text, start + 1, end - 1);
}

const isPalindromeIterative = (text) => {
  let start = 0; 
  let end = text.length - 1;

  while (start < end) {
    if (text[start] !== text[end]) return false;
    start += 1;
    end -= 1;
  }

  return true;
}

const a = 'A man, a plan, a canal: Panama';
const res = isPalindrome(a);
console.log(`Expecting true: ${res}`);

const b = 'race a car';
const res2 = isPalindrome(b);
console.log(`Expecting false: ${res2}`);
