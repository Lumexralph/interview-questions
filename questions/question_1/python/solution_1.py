class Node(object):
    # create the linkedlist node
    def __init__(self, val):
      self.val = val
      self.next = None

  #  I can create a LinkedList class that keeps track of
  # the head, tail
class Solution:
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

l1 = Solution().generate_linked_list(112)
l2 = Solution().generate_linked_list(345)
result = Solution().addTwoNumbers(l1, l2)

while result:
    print(result.val)
    result = result.next