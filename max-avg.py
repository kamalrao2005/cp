class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k

def main():
    try:
        nums_input = input("Enter numbers (space-separated): ").strip()
        k_input = input("Enter k (positive integer): ").strip()
        
        nums = [int(x) for x in nums_input.split()]
        k = int(k_input)
        sol = Solution()
        result = sol.findMaxAverage(nums, k)
        print(f"Maximum average of subarrays with length {k}: {result}")

    except ValueError as ve:
        print(f"Value error: {ve}")
if __name__ == "__main__":
    main()
