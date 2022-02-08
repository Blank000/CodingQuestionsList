class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # I am thinking of moving from back 
        numberOfFleets = 0
        positionAndSpeed = [(position[i], speed[i]) for i in range(len(position))]
        positionAndSpeed.sort(reverse=True)
        lastTime = 0
        res = 0
        for i in range(len(positionAndSpeed)):
            pstn, sp = positionAndSpeed[i]
            time = (target-pstn)/sp
            if time > lastTime:
                res += 1
                lastTime = time
        return res
                