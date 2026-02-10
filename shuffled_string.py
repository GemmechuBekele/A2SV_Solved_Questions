class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        ordered_list = [""]*len(s)
        for char, index in zip(s, indices):
            ordered_list[index] = char

        ordered_string = "".join(ordered_list)
        return ordered_string