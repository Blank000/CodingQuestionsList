class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # The crux of the question is that if the final direction is North then the robot 
        # cannot be in infinite loop ever
        x, y = 0, 0
        currDir = "N"
        for dir in instructions:
            if dir == "G":
                if currDir == "N":
                    y += 1
                elif currDir == "S":
                    y -= 1
                elif currDir == "E":
                    x += 1
                else:
                    x -= 1
            elif dir == "L":
                if currDir == "N":
                    currDir = "W"
                elif currDir == "S":
                    currDir = "E"
                elif currDir == "E":
                    currDir = "N"
                else:
                    currDir = "S"
            elif dir == "R":
                if currDir == "N":
                    currDir = "E"
                elif currDir == "S":
                    currDir = "W"
                elif currDir == "E":
                    currDir = "S"
                else:
                    currDir = "N"
        if x == 0 and y == 0:
            return True
        if currDir == "N":
            return False
        return True