class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1_freq = [0] * 26
        s2_freq = [0] * 26

        for i in range(len(s1)):
            s1_ind = ord(s1[i]) - ord("a")
            s2_ind = ord(s2[i]) - ord("a")
        
            s1_freq[s1_ind]+=1
            s2_freq[s2_ind]+=1
        
        if s1_freq == s2_freq:
            return True
        
        left = 0
        for i in range(len(s1), len(s2)):

            old_ind = ord(s2[left]) - ord("a")
            s2_freq[old_ind] -=1
            left+=1

            new_ind = ord(s2[i]) - ord("a")
            s2_freq[new_ind]+=1

            if s1_freq == s2_freq:
                return True
        
        return s1_freq == s2_freq
