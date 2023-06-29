def rearrange_array(nums, n):
    result = []
    i = 0
    j = n

    while i < n and j < 2 * n:
        result.append(nums[i])
        result.append(nums[j])
        i += 1
        j += 1

    return result


nums = [2, 5, 1, 3, 4, 7]
n = 3

result = rearrange_array(nums, n)
print(result)  # Output: [2, 3, 5, 4, 1, 7]
