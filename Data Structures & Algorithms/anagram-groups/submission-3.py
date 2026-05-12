class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initial thoughts, what does this problem actually ask
        # It's asking us for numbers that have the same counts as others
        # We can use a bucket sort approach by having buckets with specific counts
        # This reduces space complexity to O(n) and time complexity to O(n)

        hashedCounts = {}
        for string in strs:
            count = [0] * 26
            for character in string:
                count[ord(character) - 97] +=1

            count = tuple(count)
            if count in hashedCounts:
                hashedCounts[count].append(string)
            else:
                hashedCounts[count] = [string]
        
        return list(hashedCounts.values())

            