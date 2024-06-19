nums = eval(input("Enter the list :"))
nums = sorted(nums)
print(nums)
diff = nums[1]-nums[0]
for i in range(1, len(nums)-1):
    if len(nums) < 2:
        print("Invalid")
        break
    else:
        if diff > nums[i+1]-nums[i]:
            continue
        elif diff == nums[i+1]-nums[i]:
            print([nums[i], nums[i+1]])
        else:
            diff = nums[i+1]-nums[i]
    print(diff)
    print([nums[i], nums[i+1]])





