class Node(object):
    # create the linkedlist node
    def __init__(self, val):
      self.val = val
      self.next = None



# Solution 1
class Solution:
    def addTwoNumbers(self, l1: Node, l2: Node) -> Node:
        dummy_head: Node = Node(0)
        p: Node = l1
        q: Node = l2
        current: Node = dummy_head
        carry: int = 0

        while (p != None or q != None):
            x: int = p.val if p != None else 0
            y: int = q.val if q != None else 0

            add: int = carry + x + y
            carry = add // 10

            current.next = Node(add % 10)
            current = current.next

            if p != None: p = p.next
            if q != None: q = q.next

        if carry > 0: current.next = Node(carry)

        return dummy_head.next

# ==========================================================================
# Solution 2
# ==========================================================================
class SolutionB:
    def addTwoNumbers(self, l1, l2 ,c = 0):
        """
        :type l1: Node
        :type l2: Node
        :rtype: Node
        """
        val = l1.val + l2.val + c
        c = val // 10
        ret = Node(val % 10 )

        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = Node(0)
            if l2.next == None:
                l2.next = Node(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
        return ret


# ==========================================================================
# Solution 3
# ==========================================================================


  #  I can create a LinkedList class that keeps track of
  # the head, tail
class SolutionC:
    def addTwoNumbers(self, l1, l2, c = 0):
      # get value in both linked list
      result = self.retrive_values(l1) + self.retrive_values(l2)
      return self.generate_linked_list(result)

    def retrive_values(self, l_list):
      """to retrive value or numbers in the linked list"""
      copy_list = l_list
      generated_data = ''
      data_length = 0

      while copy_list:
        generated_data = str(copy_list.val) + generated_data[:data_length]
        # progress through the list
        copy_list = copy_list.next
        data_length = len(generated_data)

      return int(generated_data)

    def generate_linked_list(self, num):
      """creates a linked list in reversed sequence of data"""
      # create string representation for the number
      str_num = str(num)
      # linked_list = Node(num[-1])
      head_node = None
      current_node = None
      for i in range(-1, -(len(str_num) + 1), -1):
        if not head_node:
          head_node = Node(str_num[i])
          current_node = head_node
          continue

        new_node = Node(str_num[i])
        current_node.next = new_node
        current_node = new_node

      return head_node

l1 = SolutionC().generate_linked_list(112)
l2 = SolutionC().generate_linked_list(345)
result = Solution().addTwoNumbers(l1, l2)

while result:
    print(result.val)
    result = result.next