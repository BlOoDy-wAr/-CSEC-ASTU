class Solution(object):
    def addStrings(self, num1, num2):
            i = len(num1) - 1
            j = len(num2) - 1
            carry = 0
            result = ""

            while i >= 0 or j >= 0 or carry > 0:
                if i >= 0:
                    carry += int(num1[i])
                    i -= 1
                if j >= 0:
                    carry += int(num2[j])
                    j -= 1
                
                result = str(carry % 10) + result
                carry = carry // 10

            return result