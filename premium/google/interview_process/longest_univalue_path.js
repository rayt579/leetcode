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
  return 0 ;
};

const max_path = (node, val) => {
  if (node.left == null && node.right == null)
    return 1
}


a = new TreeNode(1);
a.left = new TreeNode(4);
a.left.left = new TreeNode(4);
a.left.right = new TreeNode(4);
a.right = new TreeNode(5);
a.right.right = new TreeNode(5);

res = longestUnivaluePath(a);
console.log(`Expected 3: ${res}`);
