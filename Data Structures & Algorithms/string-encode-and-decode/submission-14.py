class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
                result += str(len(s)) + "é" + s
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            length =""
            while s[i] != "é":
                length += s[i]
                i += 1
            result.append(s[i+1:i+1+int(length)])
            i = i + 1+ int(length)
        return result

