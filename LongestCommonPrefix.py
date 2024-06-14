'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings'''

def longest_common_prefix(str):
    if not str:
        return " "
    str.sort()
    prefix = str[0]
    for s in str[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return "/"

    return prefix


strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))

strings = ["dog", "racecar", "car"]
print(longest_common_prefix(strings))

