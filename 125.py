class Solution:
    def isPalindrome(self, s: str) -> bool:
        #convert the string into alphanumeric lower case
        #check if it reads the same forwards and backwards
        string = ""
        for l in s:
            if l.isalnum():
                if l.isalpha():
                    l = l.lower()
                string+=l                
        return string == string[::-1]

            

        
