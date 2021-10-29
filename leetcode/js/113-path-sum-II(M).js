/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {number[][]}
 */
 var pathSum = function(root, targetSum) {
    
  let answers = []
  
  
  function dfs(node, target, paths = []) {
      if (!node) return

      if (node.val == target && !node.left && !node.right) {
          answers.push([...paths, node.val])
          return
      } 
      
      dfs(node.left, target - node.val, [...paths, node.val])
      dfs(node.right, target - node.val, [...paths, node.val])
  }
  
  dfs(root, targetSum)
  return answers
  
};
