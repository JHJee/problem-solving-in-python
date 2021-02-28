# https://leetcode.com/problems/valid-palindrome/submissions/
s = s.lower()
ss = "".join(c for c in s if c.isalnum())
for i in range(len(ss)):
    if ss[i] is not ss[-1 - i]:
        return False
return True
