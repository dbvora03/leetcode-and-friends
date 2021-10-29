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
 * @return {void} Do not return anything, modify root in-place instead.
 */

 var flatten = function(root) {
    
  let newNode = new TreeNode(0)
  let traverse = newNode
  
  function recursion(node) {
      
      if(!node) return null
      
      let left = node.left
      let right = node.right
      
      traverse.left = null
      traverse.right = node
      traverse = traverse.right
      
      recursion(left)
      recursion(right)
     
  }
  
  recursion(root)
  root = newNode.right
};
