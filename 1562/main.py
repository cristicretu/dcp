"""
14.11.2023

Consider the following scenario: there are N mice and N holes placed at integer points along a line. Given this, find a method that maps mice to holes such that the largest number of steps any mouse takes is minimized.

Each move consists of moving one mouse one unit to the left or right, and only one mouse can fit inside each hole.

For example, suppose the mice are positioned at [1, 4, 9, 15], and the holes are located at [10, -5, 0, 16]. In this case, the best pairing would require us to send the mouse at 1 to the hole at -5, so our function should return 6.
"""


class Solution:
    # O(nlogn)
    def assign_mice_to_holes(self, mice, holes):
        if mice is None or len(mice) < 1:
            return "No mice!"

        if holes is None or len(holes) < 1:
            return "No holes!"

        if len(mice) != len(holes):
            return "Lengths must be equal!"

        mice.sort()
        holes.sort()

        length = len(mice)
        result = 0

        for i in range(length):
            result = max(result, abs(mice[i] - holes[i]))

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.assign_mice_to_holes([1, 4, 9, 15], [10, -5, 0]))
    print(solution.assign_mice_to_holes([1, 4, 9, 15], [10, -5, 0, 16]))
    print(solution.assign_mice_to_holes([4, -4, 2], [4, 0, 5]))
    print(solution.assign_mice_to_holes([4, -4, 2], []))
    print(
        solution.assign_mice_to_holes(
            [-10, -79, -79, 67, 93, -85, -28, -94], [-2, 9, 69, 25, -31, 23, 50, 78]
        )
    )
    print(
        solution.assign_mice_to_holes(
            [78, -82, 92, 65, -85, 99, -94, -58, 41, 62],
            [-46, -84, -95, -35, 76, -99, -92, -40, -86, -69],
        )
    )
    print(
        solution.assign_mice_to_holes(
            [],
            [2, 22, 32, -58, 35, 53, 70, 79, -2, -43],
        )
    )
    print(
        solution.assign_mice_to_holes(
            [-23, 35, 82, 58, 35, -2, -73, -52, 22, 75],
            [2, 22, 32, -58, 35, 53, 70, 79, -2, -43],
        )
    )
    print(
        solution.assign_mice_to_holes(
            [66, -71, 72, -60, 42, 82, -73, -22, 61, -75],
            [-46, 89, 13, -86, 58, -96, -94, -93, -83, 49],
        )
    )
