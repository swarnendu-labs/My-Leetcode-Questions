class Solution:
    def reversePairs(self, nums):
        def sort(arr):
            n = len(arr)
            if n <= 1:
                return arr, 0
            mid = n // 2
            left, c1 = sort(arr[:mid])
            right, c2 = sort(arr[mid:])
            count = c1 + c2
            j = 0
            for x in left:
                while j < len(right) and x > 2 * right[j]:
                    j += 1
                count += j
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, count

        return sort(nums)[1]