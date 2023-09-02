class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None:
            return ""
        if len(strs) == 1:
            return strs[0]
        longest_prefix = ""
        for char_index in range(len(strs[0])):
            for word_index in range(1, len(strs)):
                if char_index < len(strs[word_index]):
                    if strs[0][char_index] != strs[word_index][char_index]:
                        return longest_prefix
                else:
                    return longest_prefix
            longest_prefix += strs[0][char_index]
        return longest_prefix
        