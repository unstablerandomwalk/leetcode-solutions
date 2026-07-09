class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def nextArr(arr):
            temp = [1]
            for i in range(len(arr)-1):
                temp.append(arr[i]+arr[i+1])
            temp.append(1)
            return temp
        temp = [[1]]
        for i in range(numRows-1):
            temp.append(nextArr(temp[-1]))
        return temp