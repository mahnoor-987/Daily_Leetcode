class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for i in s:
            if i.isalnum():
                temp.append(i.lower())
        temp = ''.join(temp)
        reverse = temp[::-1]
        if(reverse == temp):
            return True
        return False
    # Time Complexity = O(n)
    # Space Complexity = O(n)
