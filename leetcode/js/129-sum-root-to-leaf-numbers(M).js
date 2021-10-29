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
 * @return {number}
 */
 var sumNumbers = function(root) {
    
  let answers = []
  
  function dfs(node, sum) {
      
      if (!node) return 
      
      sum *= 10
      sum += node.val
      
      if (!node.right && !node.left) {
          answers.push(sum)
      }
      
      dfs(node.left, sum)
      dfs(node.right, sum)
              
  }
  
  let summation = 0
  dfs(root, 0)
  
  for(const value of answers) {
      summation += value
  }
  
  return summation

};