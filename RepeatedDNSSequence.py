class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # base case
        if len(s) < 10:
            return []
        
        set1 = set()
        result = set()
        
        for i in range(len(s) - 9):
            substring = s[i:i+10]
            if substring in set1:
                result.add(substring)
            set1.add(substring)
        
        return list(result)

        # TC : O(n)