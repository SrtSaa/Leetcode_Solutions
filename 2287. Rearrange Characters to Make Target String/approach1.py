class Solution:
    def rearrangeCharacters(self, text: str, target: str) -> int:
        n = len(text)
        flag = [0]*n

        count = 0
        while True:
            for ch in target:
                found = False
                for i in range(n):
                    if text[i] == ch and flag[i] == 0:
                        flag[i] = 1
                        found = True
                        break
                if not found:
                    return count
            count += 1


# Time Complexity: O(k * n * m) where n is the length of text and m is the length of target and k is the number of times we can form the target string from text. In the worst case, k can be O(n/m) when all characters in text are the same as those in target.
# Space Complexity: O(n) for the flag array to keep track of used characters in text