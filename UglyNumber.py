'''An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.



Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.'''


n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Invalid input.")
else:
    if n == 1:
        print("ugly number")
    else:
        is_ugly = True
        for i in [2, 3, 5]:
            while n % i == 0:
                n //= i
        if n == 1:
            print("ugly number")
        else:
            print("not an ugly number")
