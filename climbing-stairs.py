class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        one, two = 2, 1
        for _ in range(3, n + 1):
            one, two = one + two, one
        return one
def main():
    try:
        n = int(input("Enter n (number of stairs): ").strip())
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    sol = Solution()
    result = sol.climbStairs(n)
    print(result)
if __name__ == "__main__":
    main()
