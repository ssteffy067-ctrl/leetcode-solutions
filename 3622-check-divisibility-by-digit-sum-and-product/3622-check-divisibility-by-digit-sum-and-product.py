class Solution:
    def checkDivisibility(self, n: int) -> bool:
        return n%(sum(q:=[*map(int,str(n))])+prod(q))==0
        