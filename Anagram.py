'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false'''


s = input("enter the string 1 :")
t = input("enter the string 2 :")
if s.isalpha() and t.isalpha():
    if len(s) != len(t):
        print("Not anagram")
    elif sorted(s) == sorted(t):
        print("anagrams")
    else:
        print("not anagrams")
else:
    print("enter only string/alphabet data type.")
