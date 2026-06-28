class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        while numbers[start] + numbers[end] != target:
            s = numbers[start] + numbers[end]
            if s > target:
                end -=1
            else:
                start +=1
        return [start+1, end+1]