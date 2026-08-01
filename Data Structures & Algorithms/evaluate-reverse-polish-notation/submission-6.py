class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        operators = "+-*/"
        for token in tokens:
            if token in operators:
                num1 = int(nums.pop())
                num2 = int(nums.pop())
                match token:
                    case "+":
                        res = num1+num2
                    case "-":
                        res= num2-num1
                    case "*":
                        res = num1*num2
                    case "/":
                        res = num2/num1
                nums.append(res)
            else:
                nums.append(token)
        return int(nums[0])

        