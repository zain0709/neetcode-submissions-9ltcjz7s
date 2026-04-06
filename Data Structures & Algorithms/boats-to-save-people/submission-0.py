class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people) - 1
        boats = 0
        people = sorted(people)

        while l <= r:

            if people[r] == limit:
                boats += 1
                r -= 1
            elif people[r] + people[l] <= limit:
                l += 1
                r -= 1
                boats += 1
            else:
                boats += 1
                r -= 1
        return boats
            