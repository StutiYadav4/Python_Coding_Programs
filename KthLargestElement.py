import rando


def partition(nums, left, right, pivot_index):
    pivot_value = nums[pivot_index]
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    store_index = left
    for i in range(left, right):
        if nums[i] > pivot_value:
            nums[store_index], nums[i] = nums[i], nums[store_index]
            store_index += 1
    nums[right], nums[store_index] = nums[store_index], nums[right]

    return store_index

def quickselect(nums, left, right, k):
    if left == right:
        return nums[left]
    pivot_index = random.randint(left, right)
    pivot_index = partition(nums, left, right, pivot_index)
    if k == pivot_index:
        return nums[k]
    elif k < pivot_index:
        return quickselect(nums, left, pivot_index - 1, k)
    else:
        return quickselect(nums, pivot_index + 1, right, k)


def findKthLargest(nums, k):
    return quickselect(nums, 0, len(nums) - 1, k - 1)


print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
