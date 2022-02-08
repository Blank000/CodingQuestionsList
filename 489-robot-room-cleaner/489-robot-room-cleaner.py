# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # So this is basically a DFS problem, where we are gonna ask the robot to do DFS and clean the entire room
        dirn = [(0, 1), (1, 0), (0, -1), (-1, 0)] # Up, Right, Down, Left ( When robot turns right and move, this is what happens )
        def moveBack(robot):
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
        visited = {}
        currCord = (0, 0)
        def dfs(robot, dirIdx, currCord):
            visited[currCord] = True
            robot.clean()
            for i in range(4): # Here it means that the robot is taking a right turn so accordingly the direction will change
                newDirnIdx = (i+dirIdx)%4
                newCord = (currCord[0]+dirn[newDirnIdx][0], currCord[1]+dirn[newDirnIdx][1])
                if newCord not in visited and robot.move():
                    dfs(robot, newDirnIdx, newCord)
                    moveBack(robot)
                robot.turnRight()
        dfs(robot, 0, currCord)
            
            
            