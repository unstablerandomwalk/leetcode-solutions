class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = {}
        for i in range(len(position)):
            time[position[i]] = (target - position[i]) / speed[i]
        time = sorted(time.items(), key=lambda item: item[0], reverse=True)
        count = 0
        maxTime = 0
        for i in time:
            if i[1] > maxTime:
                maxTime = i[1]
                count += 1
        return count
