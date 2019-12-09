from __future__ import annotations


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # validations
        if not isinstance(nums, list) or not isinstance(target, int):
            return []

        # since we would have to review an element that matches
        # keeping a store of visited element for future reference
        visited = {}

        # go through the nums sequence
        # store any visited element and its index
        # look for the remaining value to complete
        # the sum from the store hashmap
        for i in range(len(nums)):
            # validation
            if not isinstance(nums[i], int):
                return []

            index = visited.get(target - nums[i])

            if index is not None:
                # we have found the element to make up the sum
                return [index, i]

            # store the visited element if there's no match
            visited[nums[i]] = i

        return []
