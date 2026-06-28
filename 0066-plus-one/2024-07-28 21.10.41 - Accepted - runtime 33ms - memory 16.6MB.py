class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        l = []
        for x in range(len(digits)):
            number = number*10 + digits[x]
        number += 1
        for y in range(len(str(number))):
            l.append(number%10)
            number = number // 10
        l.reverse()
        return l