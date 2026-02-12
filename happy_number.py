class Solution:
    def isHappy(self, n: int) -> bool:

        #track what seen
        n_set = set()
        flag = True
        while flag: 
            if n == 1:
                return True

            if n in n_set:
                return False
            n_set.add(n)

            numstr = str(n) 
            sumsqr = 0

            for j in numstr:
                strnum = int(j)
                sumsqr += (strnum**2)

            n = sumsqr 
        return False
