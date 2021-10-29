/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
 var addTwoNumbers = function(l1, l2) {


  // Create a temporary reference node  
  const head = new ListNode(0)
  let traverse = head

  let carry = 0

  // Traverse until you get through every single node
  while (l1 || l2) {

    // Set our values
    let l1val = l1 ? l1.val : 0
    let l2val = l2 ? l2.val : 0

    let sum = l1val + l2val + carry;

    if (sum > 9) {
      sum = sum % 10
      carry = 0
    }

    if (l1) l1 = l1.next
    if (l2) l2 = l2.next

    let newNode = new ListNode(sum)
    traverse.next = newNode
    traverse = traverse.next

  }

  if (carry == 1) {
    traverse.next = new ListNode(1)
  }

  return head.next
};