class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        result = []
        for word in strs:
            key = "".join(sorted(word))
            hashmap[key] = [word] + hashmap.get(key,[])
        return list(hashmap.values())