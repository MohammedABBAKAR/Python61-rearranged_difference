# Rearrange the Number
# Given a number, return the difference between the maximum and minimum numbers
# that can be formed when the digits are rearranged.

# Examples
# rearranged_difference(972882) ➞ 760833
# # 988722 - 227889 = 760833

# rearranged_difference(3320707) ➞ 7709823
# # 7733200 - 23377 = 7709823

# rearranged_difference(90010) ➞ 90981
# # 91000 - 19 = 90981
# Notes
# N/A


def rearranged_difference(num):
    # Convert the number to a string, then sort the digits to form max and min numbers
    digits = list(str(num))
    
    # Get the maximum number by sorting digits in descending order
    max_num = int(''.join(sorted(digits, reverse=True)))
    
    # Get the minimum number by sorting digits in ascending order, removing leading zeros
    min_num = int(''.join(sorted(digits)))
    
    # Return the difference between the maximum and minimum number
    return max_num - min_num

# Test cases
print(rearranged_difference(972882))  # ➞ 760833
print(rearranged_difference(3320707))  # ➞ 7709823
print(rearranged_difference(90010))  # ➞ 90981
