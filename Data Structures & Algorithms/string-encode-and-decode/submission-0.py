class Solution:
    def encode(self, strs: List[str]) -> str:
        new_string=""
        for string in strs:
            new_string +="$" + str(len(string)) + "$" + string
        return new_string

    def decode(self, s: str) -> List[str]:
       res = []
       num=""
       i= 1
       while i < len(s):
           if s[i] == "$":
               length = int(num)
               word = s[i+1 : i + length + 1]
               res.append(word)
               num=""
               i+=length+2
           else:
               num+= s[i]
               i += 1
       return res
    

    
