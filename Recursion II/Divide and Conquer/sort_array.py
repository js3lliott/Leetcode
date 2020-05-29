class Solution:

    def sortArray(self, nums):

        # Merge Sort Iterative solution
        def mergeSort(self, nums):
            if len(nums) > 1:
                mid = len(nums) // 2
                left = nums[:mid]
                right = nums[mid:]

                self.mergeSort(left)
                self.mergeSort(right)

                i = 0
                j = 0
                k = 0

                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        nums[k] = left[i]
                        i += 1
                    else:
                        nums[k] = right[j]
                        j += 1

                    k += 1

                while i < len(left):
                    nums[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    nums[k] = right[j]
                    j += 1
                    k += 1

            return nums


        # Quick Sort solution
        def quickSort(self, nums):
            def helper(head, tail):
                if head >= tail:
                    return 
                left, right = head, tail
                mid = (right - left) // 2 + left

                pivot = nums[mid]

                while right >= left:
                    while right >= left and nums[left] < pivot:
                        left += 1
                    while right >= left and nums[right] > pivot:
                        right -= 1

                    if right >= left:
                        nums[left], nums[right] = nums[right], nums[left]
                        left += 1
                        right -= 1

                helper(head, right)
                helper(left, tail)

            helper(0, len(nums) - 1)
            return nums


        # Bubble Sort solution
        def bubbleSort(self, nums):
            n = len(nums)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if nums[j] > nums[j + 1]:
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
            return nums


        # Insertion Sort solution
        def insertionSort(self, nums):
            for i in range(1, len(nums)):
                key = nums[i]
                j = i - 1
                while j >= 0 and key < nums[j]:
                    nums[j + 1] = nums[j]
                    j -= 1
                nums[j + 1] = key
            return nums


        # Selection Sort solution
        def selectionSort(self, nums):
            for i in range(len(nums)):
                _min = min(nums[i:])
                min_index = nums[i:].index(_min)
                nums[i + min_index] = nums[i]
                nums[i] = _min
            return nums


        # Heap Sort solution
        def heapSort(self, nums):
            def heapify(nums, n, i):
                largest = i

                left = 2 * i + 1
                right = 2 * i + 2

                if left < n and nums[i] < nums[left]:
                    largest = left
                
                if right < n and nums[largest] < nums[right]:
                    largest = right

                if largest != i:
                    nums[i], nums[largest] = nums[largest], nums[i]

                    heapify(nums, n, largest)

            n = len(nums)

            for i in range(n, -1, -1):
                heapify(nums, n, i)

            for i in range(n - 1, 0, -1):
                nums[i], nums[0] = nums[0], nums[i]
                heapify(nums, i, 0)