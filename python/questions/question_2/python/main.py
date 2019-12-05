class Solution:
    # have list to keep track of counts
    records = {}
    def length_of_longest_substring(self, s):
      # iterate through the string without repeat of characters
      initial_length = 0
      current_length = 0
      for char in s:
        val = Solution.records.get(char)
        if not val:           # doesn't yet exist
          Solution.records[char] = 1    # add to records
          current_length += 1
        else:                 # if the character exist
          # reset current count and record
          current_length = 0
          Solution.records = {}
          continue

        if current_length > initial_length:
            initial_length = current_length

      # free up record space for garbage collection
      Solution.records = None
      current_length = None
      return initial_length

print(Solution().length_of_longest_substring('abrkaabcdefghijjxxx'))
  # 10
