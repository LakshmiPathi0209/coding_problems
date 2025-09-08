class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        direction = [0,  1]
        position =  [0 , 0]

        loop_instruction = instructions * 4

        for i in loop_instruction:

            if i == "G":
                position[0] += direction[0]
                position[1] += direction[1]

            elif i == "L":
                direction[0], direction[1] = direction[1] * -1, direction[0]

            elif i == "R":
                direction[0], direction[1] = direction[1] , direction[0]* -1
        return True if position[0] == 0 and position[1] == 0 else False


if __name__ == "__main__":
    obj = Solution()
    print(obj.isRobotBounded("GR"))


