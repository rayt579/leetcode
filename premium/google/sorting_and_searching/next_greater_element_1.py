class Solution:
    def nextGreaterElement(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        next_greater_value, stack = {}, []
        for num in nums2:
            while len(stack) > 0 and stack[-1] < num:
                next_greater_value[stack.pop()] = num
            stack.append(num)
        return [next_greater_value[n] if n in next_greater_value else -1 for n in nums1]

sol = Solution()
asc = [1,2,3,4,5]
desc = [5, 4, 3, 2, 1, 10]
res_asc = sol.nextGreaterElement([2, 3], asc)
res_desc = sol.nextGreaterElement([2, 3], desc)
print('Expecting <3, 4> : {}'.format(res_asc))
print('Expecting <10, 10> : {}'.format(res_desc))
