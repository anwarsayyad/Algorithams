def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort(key=lambda x : x[1])
        cur,ans = float('-inf'),0

        for pair in pairs:
            if cur < pair[0]:
                cur = pair[1]
                ans += 1
        
        return ans