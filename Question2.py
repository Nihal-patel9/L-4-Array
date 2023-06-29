def find_disjoint_nums(nums1, nums2):
    distinct_nums1 = set(nums1)
    distinct_nums2 = set(nums2)

    answer = [[], []]

    for num in nums1:
        if num not in distinct_nums2:
            answer[0].append(num)

    for num in nums2:
        if num not in distinct_nums1:
            answer[1].append(num)

    return answer


nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

result = find_disjoint_nums(nums1, nums2)
print(result)  # Output: [[1, 3], [4, 6]]
