class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        st = [] # (position, speed, index)
        time = [float("inf")]*len(cars)
        for i in range(len(cars)-1, -1, -1):
            while st and cars[i][1] <= st[-1][1]:
                st.pop()
            while st and cars[i][1] > st[-1][1]:
                relSpeed = cars[i][1] - st[-1][1]
                relTime = (st[-1][0]-cars[i][0]) / relSpeed
                if relTime <= time[st[-1][2]]:
                    time[i] = relTime
                    break
                else:
                    st.pop()
            
            st.append((cars[i][0], cars[i][1], i))
        for i in range(len(time)):
            if time[i] == float("inf"):
                time[i] = -1
        return time