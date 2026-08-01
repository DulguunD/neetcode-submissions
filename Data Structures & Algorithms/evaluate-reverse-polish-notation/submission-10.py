class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        operators = "+-*/"
        for token in tokens:
            if token in operators:
                num1 = nums.pop()
                num2 = nums.pop()
                match token:
                    case "+":
                        nums.append(num1+num2)
                    case "-":
                        nums.append(num2-num1)
                    case "*":
                        nums.append(num1*num2)
                    case "/":
                        nums.append((int)(num2/num1))
            else:
                nums.append(int(token))
        return nums.pop()

        