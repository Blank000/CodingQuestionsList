class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        i = 0
        while i < len(asteroids):
            if len(st) == 0:
                st.append(asteroids[i])
            elif st[-1]*asteroids[i] > 0 or asteroids[i] > 0:
                st.append(asteroids[i])
            else:
                #print("asdfghj ", str(asteroids))
                currAsteroid = asteroids[i]
                doubleExplosion = False
                while st and st[-1]*currAsteroid < 0:
                    prevAsteroid = st.pop()
                    if abs(prevAsteroid) > abs(currAsteroid):
                        st.append(prevAsteroid)
                        break
                    elif abs(prevAsteroid) == abs(currAsteroid):
                        doubleExplosion = True
                        break
                if not doubleExplosion and ((st and st[-1]*currAsteroid > 0) or (len(st) == 0)):
                    st.append(currAsteroid)
            i += 1
        return st