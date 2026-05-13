class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
                result += str(len(s)) + "é" + s
        print("Encode result: ", result)
        return result


    def decode(self, s: str) -> List[str]:
        print('Decoding: ', str)
        result = []
        i = 0
        # while i < len(s):
        #         if s[i].isnumeric() and s[i+1] == "é":
        #                 j = i + int(s[i]) + 2
        #                 result.append(s[i+2:j])
        #                 i = j - 1
        #         i += 1
        while i < len(s):
            length =""
            while s[i] != "é":
                length += s[i]
                i += 1
            result.append(s[i+1:i+1+int(length)])
            i = i + 1+ int(length)
            # l = i
            # if s[i] == "é":

        #     while s[i].isnumeric():
        #         temp += s[i]
        #         i += 1
        #         print(temp)
        #     if s[i] == "é":
        #         i -= 1
        #         m = int(temp) if temp else 0
        #         result.append(s[i:l+m])
        #     i += 1
        # return result
        # return s.split("é")[:-1]
        return result

