class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                l.append(s[i])
            else:
                if not l:
                    return False

                if ((l[-1]=="(" and s[i] == ")") or (l[-1]=="{" and s[i] == "}") or (l[-1]=="[" and s[i] == "]")):
                    l.pop()
                else:
                    return False
        return not l