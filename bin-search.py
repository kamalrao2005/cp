class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

def main():
    try:
        # Read a list of integers from the user, e.g., "1 2 3 4 5"
        nums_input = input("Enter sorted integers (space-separated): ").strip()
        nums = [int(x) for x in nums_input.split()]
        target_input = input("Enter target integer: ").strip()
        target = int(target_input)
        sol = Solution()
        result = sol.search(nums, target)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
