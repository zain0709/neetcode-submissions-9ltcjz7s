class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_word = ""
        for word in strs:
            encoded_word += word 
            encoded_word += "###___###"

        return encoded_word
    def decode(self, s: str) -> List[str]:
        s = (s.split("###___###"))
        s = s[0:-1]
        return s
        
