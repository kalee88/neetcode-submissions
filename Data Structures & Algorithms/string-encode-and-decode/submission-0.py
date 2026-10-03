class Solution:

    def encode(self, strs: List[str]) -> str:
        return_string = ""
        for s in strs:
            return_string += f"{len(s)}#{s}"
        return return_string

    def decode(self, s: str) -> List[str]:
        return_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            return_list.append(s[i : i + length])
            i += length 
        return return_list
