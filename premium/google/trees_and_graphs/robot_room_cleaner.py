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
    def __init__(self):
        self.direction_i = None

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()

        # LEFT DOWN RIGHT UP
        directions = [(0, -1), (1, 0), (0, 1), (-1,0)]
        self.direction_i = 0

        def dfs(i, j):
            coordinate = (i, j)
            if coordinate in visited:
                return 
            visited.add(coordinate)
            robot.clean()
            
            for _ in range(4):
                if robot.move():
                    next_i, next_j = i + directions[self.direction_i][0], j + directions[self.direction_i][1]
                    if (next_i, next_j) not in visited:
                        dfs(next_i, next_j)
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()

                robot.turnLeft()
                self.direction_i = (self.direction_i + 1) % 4
        dfs(0, 0)

