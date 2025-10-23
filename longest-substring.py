class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            seen[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len

def main():
    try:
        # Read a single line from the user (strip to remove trailing newline)
        s = input("Enter a string: ").strip()
        sol = Solution()
        result = solver.lengthOfLongestSubstring(s)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
