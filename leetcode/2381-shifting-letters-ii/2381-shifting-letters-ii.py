class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0]*(n+1)
        for start, end, direction in shifts:
            if direction == 1:
                arr[start] += 1
                arr[end+1] -= 1
            else:
               arr[start] -= 1
               arr[end+1] += 1
        totShift = 0
        result = []
        for i in range(n):
            totShift += arr[i]
            newChar = chr((ord(s[i]) - ord('a') + totShift) % 26 + ord('a'))
            result.append(newChar)
        return "".join(result)

        