def myPow( x: float, n: int) -> float:
        ans = 1.0
        nn = n
        if n < 0:
            nn = -1 * n
        while nn > 0:
            if nn % 2 == 1:
                ans *= x
            x *= x
            nn //= 2
        
        if  n < 0:
            return 1/ans
        return ans

print(myPow(2.0,10))