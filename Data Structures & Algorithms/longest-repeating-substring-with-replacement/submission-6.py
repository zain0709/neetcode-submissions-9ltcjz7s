class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sets = set(s)
        maxCount = 0

        for c in sets:
            count = 0
            l = 0
            fakeK = k

            for i in range(len(s)):
                if s[i] == c:
                    count += 1
                else:
                    fakeK -= 1
                    count += 1

                while fakeK < 0:
                    if s[l] != c:
                        fakeK += 1
                    count -= 1
                    l += 1

                maxCount = max(maxCount, count)

        return maxCount