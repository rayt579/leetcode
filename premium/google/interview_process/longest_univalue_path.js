/**
 * Definition for a binary tree node.
 */
function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}

/**
 * @param {TreeNode} root
 * @return {number}
 */
var longestUnivaluePath = function(root) {
  const helper = function longestPathAtNodeEqualToValue(node, val) {
    if (!node) { return 0; }
    
    var leftMaxPath = (node.left === null) ? 0 : helper(node.left, node.val);
    var rightMaxPath = (node.right === null) ? 0 : helper(node.right, node.val);
    res = Math.max(res, leftMaxPath + rightMaxPath);
    return (node.val === val) ? Math.max(leftMaxPath, rightMaxPath) + 1 : 0
  }

  let res = 0;
  helper(root, null);
  return res;
};

const a = new TreeNode(5);
a.left = new TreeNode(4);
a.left.left = new TreeNode(1);
a.left.right = new TreeNode(1);
a.right = new TreeNode(5);
a.right.left = new TreeNode(5);

const res = longestUnivaluePath(a);
console.log(`Expected 2: ${res}`);
