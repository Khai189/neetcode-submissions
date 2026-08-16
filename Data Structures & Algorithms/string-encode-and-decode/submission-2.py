class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = []

        for string in strs:
            length = str(len(string))
            encoded_str.append(length + "#" + string)
        
        return "".join(encoded_str)
    def decode(self, s: str) -> List[str]:

        res = []
        cur_ptr = 0
        cur_size = 0
        while cur_ptr < len(s):
            while s[cur_ptr] != "#" and cur_ptr < len(s):
                cur_size *=10
                cur_size += int(s[cur_ptr])
                cur_ptr+=1
            
            cur_ptr += 1  
            res.append(s[cur_ptr : cur_ptr + cur_size])  
            cur_ptr += cur_size  
            cur_size = 0
        
        return res



