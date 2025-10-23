class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
def main():
    try:
        user_input = input("Enter a string to check if it is a palindrome: ")
        sol = Solution()
        result = sol.isPalindrome(user_input)
        print("Palindrome:" if result else "Not a palindrome")
    except Exception as e:
        print(f"Unhandled error: {e}")

if __name__ == "__main__":
    main()
