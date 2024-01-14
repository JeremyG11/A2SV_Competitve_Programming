class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapOne, mapTwo = {}, {}

        if(len(s) != len(t)):
            return False
        for i in range(len(s)):
            mapOne[s[i]] = 1 + mapOne.get(s[i], 0)
            mapTwo[t[i]] = 1 + mapTwo.get(t[i], 0)

        return mapOne == mapTwo

