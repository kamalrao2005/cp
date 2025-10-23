class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        answer1 = sum(1 for x in nums1 if x in set2)
        answer2 = sum(1 for x in nums2 if x in set1)
        return [answer1, answer2]
def main():
    try:
        nums1_input = input("Enter numbers for nums1 (space-separated): ").strip()
        nums1 = [int(x) for x in nums1_input.split()] if nums1_input else []
        nums2_input = input("Enter numbers for nums2 (space-separated): ").strip()
        nums2 = [int(x) for x in nums2_input.split()] if nums2_input else []
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        return
    sol = Solution()
    result = sol.findIntersectionValues(nums1, nums2)
    print(result)
if __name__ == "__main__":
    main()
