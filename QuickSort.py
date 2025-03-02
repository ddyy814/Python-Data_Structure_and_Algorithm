
def quick_sort(nums, low, high): # low the first value in given array, high the last value in given array
    if low >= high:
        return

    pivot_index = partition(nums, low, high)
    quick_sort(nums, low, pivot_index - 1)
    quick_sort(nums, pivot_index + 1, high)


def partition(nums, low, high):

    pivot_index = (low + high) // 2 # // means integer division
    swap(nums, pivot_index, high)

    i = low

    for j in range (low, high, 1):
        if nums[j] < nums[high]:
            swap(nums, i, j)
            i = i + 1

    swap(nums, i, high)

    return i


def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


if __name__ == "__main__":

    nums = [-2,-1,0,-2,-1,0,1]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)