numbers = [float(i) for i in input().split()]

def rounding(nums):
    result = []

    if nums:
        for i in range(len(nums)):
            result.append(round(nums[i]))
    else:
        return 'Error'

    return result

print(rounding(numbers))