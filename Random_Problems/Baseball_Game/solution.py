class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for i in operations:
                if i == "+":
                        stack.append(stack[-1] + stack[-2])
                elif i == "D":
                        stack.append(2 * stack[-1])
                elif i == "C":
                        stack.pop()
                else:
                        stack.append(int(i))
                
        return sum(stack)
