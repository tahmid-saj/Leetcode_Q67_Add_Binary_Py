class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        if len(a) <= len(b):
            a = ("0" * (len(b) - len(a))) + a[0:]
        elif len(a) > len(b):
            b = ("0" * (len(a) - len(b))) + b[0:]
        
        for i in range(len(a) - 1, -1, -1):
            if carry == 0:
                if a[i] == '0' and b[i] == '0':
                    res = "0" + res[0:]
                if (a[i] == '0' and b[i] == '1') or (a[i] == '1' and b[i] == '0'):
                    res = "1" + res[0:]
                if (a[i] == '1' and b[i] == '1'):
                    res = "0" + res[0:]
                    carry = 1
            elif carry == 1:
                if a[i] == '0' and b[i] == '0':
                    res = "1" + res[0:]
                    carry = 0
                if (a[i] == '0' and b[i] == '1') or (a[i] == '1' and b[i] == '0'):
                    res = "0" + res[0:]
                if (a[i] == '1' and b[i] == '1'):
                    res = "1" + res[0:]
            
            if carry == 1 and i == 0:
                res = "1" + res[0:]
        
        return res