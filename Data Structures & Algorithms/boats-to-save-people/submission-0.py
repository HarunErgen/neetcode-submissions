class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = len(people) - 1
        j = 0
        boat = 0

        while i >= j:
            if people[i] + people[j] <= limit:
                j += 1
            boat += 1
            i -= 1
        return boat
