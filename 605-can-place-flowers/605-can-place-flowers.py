class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Solve using greedy method
        def canBePlaced(flowerbed, idx):
            if flowerbed[idx] == 1:
                return False
            if idx == 0:
                if flowerbed[idx+1] != 1:
                    return True
                return False
            elif idx == len(flowerbed)-1:
                if flowerbed[idx-1] != 1:
                    return True
                return False
            elif flowerbed[idx+1] != 1 and flowerbed[idx-1] != 1:
                return True
            return False
                
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 or n == 0:
                return True
            return False
        for i in range(len(flowerbed)):
            if canBePlaced(flowerbed, i):
                flowerbed[i] = 1
                n -= 1
                i += 1
            if n == 0:
                return True
        if n <= 0:
            return True
        return False