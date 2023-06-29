def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:
            break


def array_pair_sum(nums):

    bubble_sort(nums)

    pair_sum = 0

    for i in range(0, len(nums), 2):
        pair_sum += nums[i]

    return pair_sum


nums = [1, 4, 3, 2]

result = array_pair_sum(nums)
print(result)  # Output: 4
