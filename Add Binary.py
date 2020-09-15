class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la=len(a)
        lb=len(b)
        ca=0
        cb=0
        r=[]
        a=''.join(reversed(a))
        b=''.join(reversed(b))
        for i in range(la):
            ca += pow(2,i) * int(a[i])
        for i in range(lb):
            cb += pow(2,i) * int(b[i])
        c=ca+cb
        if c==0:
            return "0"
        while c>1:
            u=c%2
            if u==0:
                c=c//2
                r.append("0")
            else:
                c=c//2
                r.append("1")
        r.append("1")
        r=''.join(reversed(r))
        return r