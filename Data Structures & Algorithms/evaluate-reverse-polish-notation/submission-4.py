class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0
        nums = []
        operators = "+-*/"
        for token in tokens:
            if token in operators:
                # print(f"Operation: {token}")
                # operations.append(token)

                num1 = int(nums.pop())
                num2 = int(nums.pop())
                res = 0
                if token == "+":
                    res = num1+num2
                elif token == "-":
                    res= num2-num1
                elif token == "*":
                    res = num1*num2
                elif token == "/":
                    res = num2/num1
                # print(f"num1: {num1}, num2: {num2}, result = {res}")
                nums.append(res)
            else:
                # integer, num
                nums.append(token)
            # pending.append(token)
        # print(f"pending: {nums}, Operations: {operations}")
        return int(nums[0])

        