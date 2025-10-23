class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


def main():
    try:
        user_input = input("Enter a rotated sorted array of integers (space-separated): ").strip()
        nums = [int(x) for x in user_input.split()]
        sol = Solution()
        result = sol.findMin(nums)
        print(f"The minimum element is: {result}")
    except ValueError as ve:
        print(f"Value error: {ve}")

if __name__ == "__main__":
    main()
