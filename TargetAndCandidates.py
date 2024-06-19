def combinationSum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            backtrack(i, target - candidates[i], path + [candidates[i]])

    result = []
    candidates.sort()
    backtrack(0, target, [])
    return result

print(combinationSum([2, 3, 6, 7], 7))
print(combinationSum([2, 3, 5], 8))
print(combinationSum([2], 1))
